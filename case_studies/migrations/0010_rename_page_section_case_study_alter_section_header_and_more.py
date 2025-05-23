# Generated by Django 5.1.5 on 2025-03-31 17:04

import case_studies.models
import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0009_alter_casestudydata_data_content_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='page',
            new_name='case_study',
        ),
        migrations.AlterField(
            model_name='section',
            name='header',
            field=models.CharField(blank=True, help_text='Optional Header to display below section images', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='text',
            field=tinymce.models.HTMLField(blank=True, help_text='Optional text to display below section images', null=True),
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='WEBP / JPG / PNG / GIF / ratio: 3:2 / width: 1680px', upload_to=case_studies.models.upload_to)),
                ('caption', models.TextField(blank=True, help_text='Optional caption to display below an image', max_length=500, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_images', to='case_studies.section')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'ordering': ['order'],
            },
        ),
    ]
