# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_semantic_ui', '0002_tab_tabcontainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='responsive',
            field=models.CharField(choices=[(b'stackable', b'Stackable'), (b'doubling', b'Doubling'), (b'stackable doubling', b'Stackable and Doubling')], max_length=20, blank=True, help_text='Grid responsive behavior', null=True, verbose_name='Responsive'),
        ),
        migrations.AlterField(
            model_name='tab',
            name='tab_type',
            field=models.CharField(default=b'bottom attached', max_length=20, verbose_name='Tab Type', blank=True, choices=[(b'bottom attached', b'Bottom attached')]),
        ),
        migrations.AlterField(
            model_name='tabcontainer',
            name='tab_container_type',
            field=models.CharField(default=b'top attached tabular', max_length=20, verbose_name='Tab Container Type', blank=True, choices=[(b'top attached tabular', b'Top attached tabular'), (b'pointing secondary', b'Pointing secondary')]),
        ),
    ]
