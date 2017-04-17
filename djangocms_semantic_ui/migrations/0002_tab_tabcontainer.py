# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('djangocms_semantic_ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('label', models.CharField(verbose_name='Label', max_length=255, blank=True, help_text='Overrides the display name in the structure mode.')),
                ('data_tab', models.CharField(verbose_name='Datatab', max_length=255, help_text='Data_tab')),
                ('tab_type', models.CharField(verbose_name='Tab Type', max_length=20, blank=True, choices=[('bottom attached', 'Bottom attached')])),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, related_name='djangocms_semantic_ui_tab', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TabContainer',
            fields=[
                ('label', models.CharField(verbose_name='Label', max_length=255, blank=True, help_text='Overrides the display name in the structure mode.')),
                ('tab_container_type', models.CharField(verbose_name='Tab Container Type', max_length=20, blank=True, choices=[('pointing secondary', 'Pointing secondary'), ('top attached tabular', 'Top attached tabular')])),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, related_name='djangocms_semantic_ui_tabcontainer', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
