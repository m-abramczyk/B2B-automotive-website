# Generated by Django 5.1.5 on 2025-04-02 17:15

import case_studies.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0015_alter_casestudy_header_alter_casestudy_labels_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionimage',
            name='image',
            field=models.ImageField(help_text='There can be max 3 images in a section. First two images are small, third image is full width. Format: WEBP / JPG / PNG / GIF / ratio: 3:2 / width: 1680px', upload_to=case_studies.models.upload_to),
        ),
    ]
