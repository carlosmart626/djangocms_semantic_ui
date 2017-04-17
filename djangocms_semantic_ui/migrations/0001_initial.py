# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('label', models.CharField(verbose_name='Label', max_length=255, blank=True, help_text='Overrides the display name in the structure mode.')),
                ('column_width', models.CharField(verbose_name='Number Columns', max_length=20, blank=True, choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten'), ('eleven', 'eleven'), ('twelve', 'twelve'), ('thirteen', 'thirteen'), ('fourteen', 'fourteen'), ('fiveteen', 'fiveteen'), ('sixteen', 'sixteen')])),
                ('align', models.CharField(verbose_name='type_group', max_length=20, blank=True, choices=[('left floated', 'Left floated'), ('center aligned', 'Center aligned'), ('right floated', 'Right floated')])),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, related_name='djangocms_semantic_ui_column', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('label', models.CharField(verbose_name='Label', max_length=255, blank=True, help_text='Overrides the display name in the structure mode.')),
                ('type_container', models.CharField(verbose_name='type_group', max_length=20, blank=True, choices=[('left aligned', 'Left aligned'), ('center aligned', 'Center aligned'), ('right aligned', 'Right aligned'), ('justified', 'Justified')])),
                ('is_text_container', models.BooleanField(verbose_name='Text container', default=False, help_text='Check if this is a text container')),
                ('is_raised', models.BooleanField(verbose_name='Raised container', default=False, help_text='Check if this is a raised container')),
                ('is_fluid', models.BooleanField(verbose_name='Fluid container', default=False, help_text='Check if this is a Fluid container')),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, related_name='djangocms_semantic_ui_container', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('label', models.CharField(verbose_name='Label', max_length=255, blank=True, help_text='Overrides the display name in the structure mode.')),
                ('number_columns', models.CharField(verbose_name='Number Columns', max_length=20, blank=True, choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten'), ('eleven', 'eleven'), ('twelve', 'twelve'), ('thirteen', 'thirteen'), ('fourteen', 'fourteen'), ('fiveteen', 'fiveteen'), ('sixteen', 'sixteen')])),
                ('grid_type', models.CharField(verbose_name='Grid Type', max_length=20, blank=True, choices=[('relaxed', 'relaxed'), ('internally celled', 'Internally celled'), ('equal width', 'Equal width')])),
                ('align', models.CharField(verbose_name='type_group', max_length=20, blank=True, choices=[('left aligned', 'Left aligned'), ('centered', 'Centered'), ('right aligned', 'Right aligned')])),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, related_name='djangocms_semantic_ui_grid', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GroupSegment',
            fields=[
                ('label', models.CharField(verbose_name='Label', max_length=255, blank=True, help_text='Overrides the display name in the structure mode.')),
                ('type_group', models.CharField(verbose_name='type_group', max_length=20, default='vertical', choices=[('vertical', 'Vertical'), ('horizontal', 'Horizontal')])),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, related_name='djangocms_semantic_ui_groupsegment', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('label', models.CharField(verbose_name='Label', max_length=255, blank=True, help_text='Overrides the display name in the structure mode.')),
                ('color', models.CharField(verbose_name='Color', max_length=20, blank=True, null=True, choices=[('red', 'Red'), ('orange', 'Orange'), ('yellow', 'Yellow'), ('olive', 'Olive'), ('green', 'Green'), ('teal', 'Teal'), ('blue', 'Blue'), ('violet', 'Violet'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('grey', 'Grey'), ('black', 'Black')], help_text='Color Segment')),
                ('inverted_color', models.BooleanField(verbose_name='Inverted Color', default=False, help_text='Inveted Color Segment')),
                ('type_segment', models.CharField(verbose_name='Type', max_length=20, blank=True, null=True, choices=[('raised', 'Raised'), ('stacked', 'Stacked'), ('tall stacked', 'Tall stacked'), ('piled', 'Piled')], help_text='Whats the type of segment')),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, related_name='djangocms_semantic_ui_segment', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
