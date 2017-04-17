from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import GroupSegment, Segment, Container, Grid, Column, TabContainer, Tab


class TabContainerForm(forms.ModelForm):

    NUM_COLUMNS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    )

    create = forms.ChoiceField(
        choices=NUM_COLUMNS,
        label=_("Create tabs"),
        help_text=_("Create this number of tabs")
    )

    class Meta:
        model = TabContainer
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class TabForm(forms.ModelForm):

    class Meta:
        model = Tab
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class GroupSegmentForm(forms.ModelForm):

    NUM_COLUMNS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    )

    create = forms.ChoiceField(
        choices=NUM_COLUMNS,
        label=_("Create Segments"),
        help_text=_("Create this number of segments")
    )

    class Meta:
        model = GroupSegment
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class SegmentForm(forms.ModelForm):

    class Meta:
        model = Segment
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class ContainerForm(forms.ModelForm):

    class Meta:
        model = Container
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class GridForm(forms.ModelForm):

    class Meta:
        model = Grid
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class ColumnForm(forms.ModelForm):

    class Meta:
        model = Column
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
