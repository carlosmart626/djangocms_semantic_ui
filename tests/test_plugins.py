"""Smoke tests that exercise every plugin through the real admin add-plugin
endpoint, plus a rendering check of the resulting page.

The GroupSegment / TabContainer cases are the important ones: their
``save_model`` auto-creates children, which used to assign
``position=CMSPlugin.objects.filter(parent=obj).count()``.  On django-cms 4+
``CMSPlugin.position`` is an absolute, unique index within
(placeholder, language), so the second auto-created child collided and raised
``IntegrityError: UNIQUE constraint failed:
cms_cmsplugin.placeholder_id, cms_cmsplugin.language, cms_cmsplugin.position``.
"""

from cms import api
from cms.models import CMSPlugin, Placeholder
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from urllib.parse import urlencode

LANGUAGE = "en"


class AdminAddPluginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_superuser(
            username="admin", email="admin@example.com", password="secret"
        )
        cls.page = api.create_page(
            title="Test page",
            template="page.html",
            language=LANGUAGE,
            created_by=cls.user,
        )
        cls.page_content = cls.page.get_content_obj(LANGUAGE)

    def setUp(self):
        self.client.force_login(self.user)
        self.placeholder = self.page_content.get_placeholders().get(slot="content")

    def add_plugin_via_admin(self, plugin_type, data=None, parent=None):
        """Drive the real admin add-plugin view and return the created plugin."""
        url = reverse("admin:cms_placeholder_add_plugin")
        position = self.placeholder.get_next_plugin_position(
            LANGUAGE, parent=parent, insert_order="last"
        )
        params = {
            "plugin_type": plugin_type,
            "placeholder_id": self.placeholder.pk,
            "plugin_language": LANGUAGE,
            "plugin_position": position,
            "cms_path": self.page.get_absolute_url(LANGUAGE),
        }
        if parent is not None:
            params["plugin_parent"] = parent.pk

        get_response = self.client.get(url, params)
        self.assertEqual(
            get_response.status_code, 200,
            "GET add-plugin for %s returned %s" % (plugin_type, get_response.status_code),
        )

        # The view validates its parameters from request.GET even on POST, so
        # they have to live in the query string; the model form data is the body.
        post_url = "%s?%s" % (url, urlencode(params))
        post_response = self.client.post(post_url, data or {})
        self.assertIn(
            post_response.status_code, (200, 302),
            "POST add-plugin for %s returned %s: %s"
            % (plugin_type, post_response.status_code, post_response.content[:2000]),
        )
        plugin = (
            CMSPlugin.objects.filter(
                placeholder=self.placeholder,
                language=LANGUAGE,
                plugin_type=plugin_type,
            )
            .order_by("-pk")
            .first()
        )
        self.assertIsNotNone(plugin, "No %s plugin was created" % plugin_type)
        return plugin

    def assert_positions_are_sane(self):
        """django-cms 4+ invariant: positions unique within (placeholder, language)."""
        positions = list(
            CMSPlugin.objects.filter(
                placeholder=self.placeholder, language=LANGUAGE
            )
            .order_by("position")
            .values_list("position", flat=True)
        )
        self.assertEqual(
            len(positions), len(set(positions)),
            "Duplicate plugin positions detected: %s" % positions,
        )

    # --- individual plugins -------------------------------------------------

    def test_simple_plugins(self):
        self.add_plugin_via_admin("ContainerPlugin", {"type_container": "left aligned"})
        self.add_plugin_via_admin("SegmentPlugin", {"color": "green", "type_segment": "raised"})
        self.add_plugin_via_admin("DividerPlugin")
        grid = self.add_plugin_via_admin("GridPlugin", {"number_columns": "two"})
        self.add_plugin_via_admin("SemanticColumnPlugin", {"column_width": "eight"}, parent=grid)
        self.add_plugin_via_admin("SemanticColumnPlugin", {"column_width": "eight"}, parent=grid)
        self.add_plugin_via_admin("TabPlugin", {"data_tab": "solo", "tab_type": "bottom attached"})
        self.assert_positions_are_sane()

    def test_group_segment_creates_children_without_integrity_error(self):
        """This is the regression case: 5 auto-created Segment children."""
        group = self.add_plugin_via_admin(
            "GroupSegmentPlugin", {"type_group": "vertical", "create": "5"}
        )
        children = CMSPlugin.objects.filter(parent=group)
        self.assertEqual(children.count(), 5, "Expected 5 auto-created segments")
        self.assertTrue(all(c.plugin_type == "SegmentPlugin" for c in children))
        self.assert_positions_are_sane()

    def test_tab_container_creates_children_without_integrity_error(self):
        container = self.add_plugin_via_admin(
            "TabContainerPlugin",
            {"tab_container_type": "top attached tabular", "create": "4"},
        )
        children = CMSPlugin.objects.filter(parent=container)
        self.assertEqual(children.count(), 4, "Expected 4 auto-created tabs")
        self.assertTrue(all(c.plugin_type == "TabPlugin" for c in children))
        labels = sorted(c.get_bound_plugin().label for c in children)
        self.assertEqual(labels, ["tab-1", "tab-2", "tab-3", "tab-4"])
        self.assert_positions_are_sane()

    def test_tab_container_child_classes_allows_tab(self):
        from cms.plugin_pool import plugin_pool

        plugin = plugin_pool.get_plugin("TabContainerPlugin")
        self.assertIn("TabPlugin", plugin.child_classes)
        self.assertIn("TabPlugin", plugin_pool.plugins)

    def test_all_plugins_together_and_page_renders(self):
        self.add_plugin_via_admin("ContainerPlugin", {"type_container": "left aligned"})
        grid = self.add_plugin_via_admin("GridPlugin", {"number_columns": "two"})
        self.add_plugin_via_admin("SemanticColumnPlugin", {"column_width": "eight"}, parent=grid)
        self.add_plugin_via_admin("SegmentPlugin", {"color": "blue"})
        self.add_plugin_via_admin("GroupSegmentPlugin", {"type_group": "horizontal", "create": "3"})
        self.add_plugin_via_admin("DividerPlugin")
        self.add_plugin_via_admin(
            "TabContainerPlugin",
            {"tab_container_type": "pointing secondary", "create": "3"},
        )
        self.assert_positions_are_sane()

        total = CMSPlugin.objects.filter(placeholder=self.placeholder).count()
        self.assertGreaterEqual(total, 12)

        response = self.client.get(self.page.get_absolute_url(LANGUAGE))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode()
        # Markup produced by the plugin templates themselves.
        self.assertIn('class="ui left aligned container"', html)
        self.assertIn('class="ui two column grid"', html)
        self.assertIn('class="eight wide column"', html)
        self.assertIn('class="ui blue segment"', html)
        # GroupSegmentPlugin renders segment.html (pre-existing behaviour) and
        # nests its auto-created Segment children inside.
        self.assertEqual(html.count('class="ui  segment"'), 4)  # group + 3 children
        self.assertIn('class="ui divider"', html)
        self.assertIn('class="ui pointing secondary menu"', html)  # TabContainer
        self.assertIn('data-tab="tab-1"', html)
        self.assertIn('data-tab="tab-3"', html)
        self.assertIn('class="ui bottom attached tab segment" data-tab="tab-1"', html)


class PlaceholderPositionInvariantTestCase(TestCase):
    def test_placeholder_model_available(self):
        self.assertTrue(hasattr(Placeholder, "objects"))
