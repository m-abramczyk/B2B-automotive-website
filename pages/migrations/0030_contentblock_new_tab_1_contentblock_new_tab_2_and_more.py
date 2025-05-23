# Generated by Django 5.1.5 on 2025-03-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_alter_contentblock_button_clients_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentblock',
            name='new_tab_1',
            field=models.BooleanField(default=False, help_text='Check to make the link open in new tab (external links)', verbose_name='Open in new tab'),
        ),
        migrations.AddField(
            model_name='contentblock',
            name='new_tab_2',
            field=models.BooleanField(default=False, help_text='Check to make the link open in new tab (external links)', verbose_name='Open in new tab'),
        ),
        migrations.AddField(
            model_name='contentblock',
            name='new_tab_clients',
            field=models.BooleanField(default=False, help_text='Check to make the link open in new tab (external links)', verbose_name='Open in new tab'),
        ),
    ]
