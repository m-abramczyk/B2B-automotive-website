# Generated by Django 5.1.5 on 2025-04-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0019_alter_sectionimage_caption'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casestudydata',
            options={'ordering': ('order',), 'verbose_name': 'Key Data Item', 'verbose_name_plural': 'Key Data Items'},
        ),
        migrations.AlterField(
            model_name='casestudydata',
            name='data_type',
            field=models.CharField(blank=True, help_text='( Year / Client / Team / Tools ) Displayed in the first column of Key Data table', max_length=60, null=True),
        ),
    ]
