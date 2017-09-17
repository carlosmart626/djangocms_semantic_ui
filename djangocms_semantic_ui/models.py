from django.db import models
from cms.models import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


SEMANTIC_UI_COLORS = (
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('yellow', 'Yellow'),
    ('olive', 'Olive'),
    ('green', 'Green'),
    ('teal', 'Teal'),
    ('blue', 'Blue'),
    ('violet', 'Violet'),
    ('purple', 'Purple'),
    ('pink', 'Pink'),
    ('brown', 'Brown'),
    ('grey', 'Grey'),
    ('black', 'Black'),
)

TYPE_SEGMENT = (
    ('raised', 'Raised'),
    ('stacked', 'Stacked'),
    ('tall stacked', 'Tall stacked'),
    ('piled', 'Piled'),
)

TEXT_CONTAINER = (
    ('left aligned', 'Left aligned'),
    ('center aligned', 'Center aligned'),
    ('right aligned', 'Right aligned'),
    ('justified', 'Justified'),
)

PADDING_CONTAINER = (
    ('very padded', 'very padded'),
    ('padded', 'padded'),
)

GROUP_SEGMENT = (
    ('vertical', 'Vertical'),
    ('horizontal', 'Horizontal'),
)

GRID_COLUMNS_WIDTH = (
    ('one', 'one'),
    ('two', 'two'),
    ('three', 'three'),
    ('four', 'four'),
    ('five', 'five'),
    ('six', 'six'),
    ('seven', 'seven'),
    ('eight', 'eight'),
    ('nine', 'nine'),
    ('ten', 'ten'),
    ('eleven', 'eleven'),
    ('twelve', 'twelve'),
    ('thirteen', 'thirteen'),
    ('fourteen', 'fourteen'),
    ('fiveteen', 'fiveteen'),
    ('sixteen', 'sixteen'),
)

GRID_TYPES = (
    ('relaxed', 'relaxed'),
    ('internally celled', 'Internally celled'),
    ('equal width', 'Equal width'),
)

GRID_ALIGN = (
    ('left aligned', 'Left aligned'),
    ('centered', 'Centered'),
    ('right aligned', 'Right aligned'),
)

GRID_RESPONSIVE = (
    ('stackable', 'Stackable'),
    ('doubling', 'Doubling'),
    ('stackable doubling', 'Stackable and Doubling'),
)

COLUMN_ALIGN = (
    ('left floated', 'Left floated'),
    ('center aligned', 'Center aligned'),
    ('right floated', 'Right floated'),
)

TAB_CONTAINER = (
    ('top attached tabular', 'Top attached tabular'),
    ('pointing secondary', 'Pointing secondary'),
)

TAB_TYPE = (
    ('bottom attached', 'Bottom attached'),
)


@python_2_unicode_compatible
class Segment(CMSPlugin):
    """
    Segment
    """
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    color = models.CharField(
        verbose_name=_('Color'),
        choices=SEMANTIC_UI_COLORS,
        max_length=20,
        null=True,
        blank=True,
        help_text=_('Color Segment'),
    )
    inverted_color = models.BooleanField(
        verbose_name=_('Inverted Color'),
        default=False,
        help_text=_('Inveted Color Segment'),
    )
    type_segment = models.CharField(
        verbose_name=_('Type'),
        choices=TYPE_SEGMENT,
        null=True,
        blank=True,
        max_length=20,
        help_text=_('Whats the type of segment'),
    )
    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return self.color or self.type_segment or str(self.pk)

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        if self.label:
            display.append(self.label)
        if self.color:
            display.append(self.color)
        if self.type_segment:
            display.append('<{0}>'.format(self.type_segment))
        return ' '.join(display)

    def get_classes(self):
        classes = []
        if self.color:
            classes.append(self.color)
        if self.type_segment:
            classes.append(self.type_segment)
        if self.inverted_color:
            classes.append('inverted')
        return ' '.join(classes)


@python_2_unicode_compatible
class GroupSegment(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    type_group = models.CharField(
        verbose_name=_('type_group'),
        choices=GROUP_SEGMENT,
        default=GROUP_SEGMENT[0][0],
        max_length=20,
    )

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return u"%s" % self.get_type_group_display()

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        if self.label:
            display.append(self.label)
        if self.type_group:
            display.append(self.type_group)
        return ' '.join(display)


@python_2_unicode_compatible
class Container(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    type_container = models.CharField(
        verbose_name=_('type_group'),
        choices=TEXT_CONTAINER,
        blank=True,
        max_length=20,
    )
    is_text_container = models.BooleanField(
        verbose_name=_('Text container'),
        default=False,
        help_text=_('Check if this is a text container'),
    )
    is_raised = models.BooleanField(
        verbose_name=_('Raised container'),
        default=False,
        help_text=_('Check if this is a raised container'),
    )
    is_fluid = models.BooleanField(
        verbose_name=_('Fluid container'),
        default=False,
        help_text=_('Check if this is a Fluid container'),
    )

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return u"%s" % self.get_type_container_display()

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        if self.label:
            display.append(self.label)
        if self.type_container:
            display.append(self.type_container)
        return ' '.join(display)

    def get_classes(self):
        classes = []
        if self.type_container:
            classes.append(self.type_container)
        if self.is_text_container:
            classes.append('text')
        if self.is_raised:
            classes.append('raise')
        if self.is_fluid:
            classes.append('fluid')
        return ' '.join(classes)


@python_2_unicode_compatible
class Grid(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    number_columns = models.CharField(
        verbose_name=_('Number Columns'),
        choices=GRID_COLUMNS_WIDTH,
        blank=True,
        max_length=20,
    )
    grid_type = models.CharField(
        verbose_name=_('Grid Type'),
        choices=GRID_TYPES,
        blank=True,
        max_length=20,
    )
    align = models.CharField(
        verbose_name=_('type_group'),
        choices=GRID_ALIGN,
        blank=True,
        max_length=20,
    )
    responsive = models.CharField(
        verbose_name=_('Responsive'),
        choices=GRID_RESPONSIVE,
        null=True,
        blank=True,
        max_length=20,
        help_text=_('Grid responsive behavior'),
    )

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return u"%s" % self.label

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        if self.label:
            display.append(self.label)
        if self.number_columns:
            display.append("cols:{}".format(self.number_columns))
        if self.grid_type:
            display.append(self.grid_type)
        return ' '.join(display)

    def get_classes(self):
        classes = []
        if self.number_columns:
            classes.append("{} column".format(self.number_columns))
        if self.grid_type:
            classes.append(self.grid_type)
        if self.align:
            classes.append(self.align)
        return ' '.join(classes)


@python_2_unicode_compatible
class Column(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    column_width = models.CharField(
        verbose_name=_('Number Columns'),
        choices=GRID_COLUMNS_WIDTH,
        blank=True,
        max_length=20,
    )
    align = models.CharField(
        verbose_name=_('type_group'),
        choices=COLUMN_ALIGN,
        blank=True,
        max_length=20,
    )

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return u"%s" % self.label

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        if self.label:
            display.append(self.label)
        if self.column_width:
            display.append("wide:{}".format(self.column_width))
        if self.align:
            display.append(self.align)
        return ' '.join(display)

    def get_classes(self):
        classes = []
        if self.column_width:
            classes.append("{} wide".format(self.column_width))
        if self.align:
            classes.append(self.align)
        return ' '.join(classes)


@python_2_unicode_compatible
class TabContainer(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    tab_container_type = models.CharField(
        verbose_name=_('Tab Container Type'),
        choices=TAB_CONTAINER,
        default=TAB_CONTAINER[0][0],
        blank=True,
        max_length=20,
    )

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return u"%s" % self.label

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        if self.label:
            display.append(self.label)
        if self.tab_container_type:
            display.append(self.tab_container_type)
        return ' '.join(display)

    def get_classes(self):
        classes = []
        if self.tab_container_type:
            classes.append(self.tab_container_type)
        return ' '.join(classes)


@python_2_unicode_compatible
class Tab(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    data_tab = models.CharField(
        verbose_name=_('Datatab'),
        max_length=255,
        help_text=_('Data_tab'),
    )
    tab_type = models.CharField(
        verbose_name=_('Tab Type'),
        choices=TAB_TYPE,
        default=TAB_TYPE[0][0],
        blank=True,
        max_length=20,
    )

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return u"%s" % self.label

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        if self.label:
            display.append(self.label)
        if self.data_tab:
            display.append(self.data_tab)
        if self.tab_type:
            display.append(self.tab_type)
        return ' '.join(display)

    def get_classes(self):
        classes = []
        if self.tab_type:
            classes.append(self.tab_type)
        return ' '.join(classes)
