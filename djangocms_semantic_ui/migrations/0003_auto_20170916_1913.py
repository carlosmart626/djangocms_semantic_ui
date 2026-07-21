from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_semantic_ui', '0002_tab_tabcontainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='responsive',
            field=models.CharField(choices=[('stackable', 'Stackable'), ('doubling', 'Doubling'), ('stackable doubling', 'Stackable and Doubling')], max_length=20, blank=True, help_text='Grid responsive behavior', null=True, verbose_name='Responsive'),
        ),
        migrations.AlterField(
            model_name='ta',
            name='tab_type',
            field=models.CharField(default='bottom attached', max_length=20, verbose_name='Tab Type', blank=True, choices=[('bottom attached', 'Bottom attached')]),
        ),
        migrations.AlterField(
            model_name='tabcontainer',
            name='tab_container_type',
            field=models.CharField(default='top attached tabular', max_length=20, verbose_name='Tab Container Type', blank=True, choices=[('top attached tabular', 'Top attached tabular'), ('pointing secondary', 'Pointing secondary')]),
        ),
    ]
