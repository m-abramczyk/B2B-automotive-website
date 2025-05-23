# Generated by Django 5.1.5 on 2025-03-24 18:57

import django.core.validators
import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_contentblock_video_caption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblock',
            name='video',
            field=models.FileField(blank=True, help_text='Overrides Image Display Type: replaces carousel with a single video: WEBM / MP4 file / recommended max size: 4Mb / length: ~30s', null=True, upload_to=pages.models.upload_to, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'webm'])]),
        ),
        migrations.AlterField(
            model_name='contentblockimage',
            name='image',
            field=models.ImageField(blank=True, help_text='WEBP / JPG / PNG / GIF / ratio: 3:2 / width: 1280px (blocks Left, Right) / width: 1680px (block Full-width)', null=True, upload_to=pages.models.upload_to),
        ),
    ]
