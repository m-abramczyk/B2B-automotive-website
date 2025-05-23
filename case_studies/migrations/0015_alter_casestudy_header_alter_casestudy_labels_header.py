# Generated by Django 5.1.5 on 2025-04-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0014_casestudy_index_cover_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='header',
            field=models.CharField(blank=True, default='Key data:', help_text='Header of Key Data block', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='labels_header',
            field=models.CharField(blank=True, default='Scope of work:', help_text='Header of labels group', max_length=60, null=True),
        ),
    ]
