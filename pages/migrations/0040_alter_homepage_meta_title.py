# Generated by Django 5.1.5 on 2025-03-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0039_alter_contentblock_video_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title', max_length=60, null=True),
        ),
    ]
