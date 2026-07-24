from cms.api import add_plugin
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import Segment, GroupSegment, Container, Column, Grid, TabContainer, Tab  # noqa: F401
from .forms import GroupSegmentForm, SegmentForm, ContainerForm, GridForm, ColumnForm, TabContainerForm, TabForm


class GridPlugin(CMSPluginBase):
    model = Grid
    module = _("Semantic UI")
    name = _('Grid')
    render_template = "djangocms_semantic_ui/grid.html"
    allow_children = True
    form = GridForm
    child_classes = ["SemanticColumnPlugin"]


class SemanticColumnPlugin(CMSPluginBase):
    model = Column
    module = _("Semantic UI")
    name = _('Column')
    render_template = "djangocms_semantic_ui/column.html"
    allow_children = True
    form = ColumnForm


class ContainerPlugin(CMSPluginBase):
    model = Container
    module = _("Semantic UI")
    name = _('Container')
    render_template = "djangocms_semantic_ui/container.html"
    allow_children = True
    form = ContainerForm


class SegmentPlugin(CMSPluginBase):
    model = Segment
    module = _("Semantic UI")
    name = _('Segment')
    render_template = "djangocms_semantic_ui/segment.html"
    allow_children = True
    form = SegmentForm


class GroupSegmentPlugin(CMSPluginBase):
    model = GroupSegment
    module = _("Semantic UI")
    name = _('Group Segment')
    render_template = "djangocms_semantic_ui/segment.html"
    allow_children = True
    form = GroupSegmentForm
    child_classes = ["SegmentPlugin"]

    def save_model(self, request, obj, form, change):
        response = super().save_model(request, obj, form, change)
        if not change:
            for _x in range(int(form.cleaned_data['create'])):
                add_plugin(
                    obj.placeholder,
                    SegmentPlugin.__name__,
                    obj.language,
                    target=obj,
                )
        return response


class DividerPlugin(CMSPluginBase):
    model = CMSPlugin
    module = _("Semantic UI")
    name = _('Divider')
    render_template = "djangocms_semantic_ui/divider.html"
    allow_children = False


class TabPlugin(CMSPluginBase):
    model = Tab
    module = _("Semantic UI")
    name = _('Tab')
    render_template = "djangocms_semantic_ui/tab.html"
    allow_children = True
    form = TabForm


class TabContainerPlugin(CMSPluginBase):
    model = TabContainer
    module = _("Semantic UI")
    name = _('Tab Container')
    render_template = "djangocms_semantic_ui/tab_container.html"
    allow_children = True
    form = TabContainerForm
    child_classes = ["TabPlugin"]

    def save_model(self, request, obj, form, change):
        response = super().save_model(request, obj, form, change)
        if not change:
            for x in range(int(form.cleaned_data['create'])):
                add_plugin(
                    obj.placeholder,
                    TabPlugin.__name__,
                    obj.language,
                    target=obj,
                    label="tab-{}".format(x + 1),
                    data_tab="tab-{}".format(x + 1),
                )
        return response


plugin_pool.register_plugin(GridPlugin)
plugin_pool.register_plugin(SemanticColumnPlugin)
plugin_pool.register_plugin(ContainerPlugin)
plugin_pool.register_plugin(SegmentPlugin)
plugin_pool.register_plugin(GroupSegmentPlugin)
plugin_pool.register_plugin(TabContainerPlugin)
plugin_pool.register_plugin(TabPlugin)
plugin_pool.register_plugin(DividerPlugin)
