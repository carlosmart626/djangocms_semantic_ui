from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Segment, GroupSegment, Container, Column, Grid, TabContainer, Tab
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
            response = super(GroupSegmentPlugin, self).save_model(
                request, obj, form, change
            )
            for x in range(int(form.cleaned_data['create'])):
                col = Segment(
                    parent=obj,
                    placeholder=obj.placeholder,
                    language=obj.language,
                    position=CMSPlugin.objects.filter(parent=obj).count(),
                    plugin_type=SegmentPlugin.__name__
                )
                col.save()
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
    child_classes = ["Tab"]

    def save_model(self, request, obj, form, change):
            response = super(TabContainerPlugin, self).save_model(
                request, obj, form, change
            )
            for x in range(int(form.cleaned_data['create'])):
                col = Tab(
                    parent=obj,
                    placeholder=obj.placeholder,
                    language=obj.language,
                    label="tab-{}".format(x + 1),
                    data_tab="tab-{}".format(x + 1),
                    position=CMSPlugin.objects.filter(parent=obj).count(),
                    plugin_type=TabPlugin.__name__
                )
                col.save()
            return response

plugin_pool.register_plugin(GridPlugin)
plugin_pool.register_plugin(SemanticColumnPlugin)
plugin_pool.register_plugin(ContainerPlugin)
plugin_pool.register_plugin(SegmentPlugin)
plugin_pool.register_plugin(GroupSegmentPlugin)
plugin_pool.register_plugin(TabContainerPlugin)
plugin_pool.register_plugin(TabPlugin)
plugin_pool.register_plugin(DividerPlugin)
