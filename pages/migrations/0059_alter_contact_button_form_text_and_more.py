# Generated by Django 5.1.5 on 2025-05-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0058_privacypolicy_accept_button_de_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='button_form_text',
            field=models.CharField(blank=True, default='Contact in a traditional way', help_text='Button scrolls to header section contact info. Max 60 characters', max_length=60, null=True, verbose_name='Contact Form button'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='button_form_text_de',
            field=models.CharField(blank=True, default='Contact in a traditional way', help_text='Button scrolls to header section contact info. Max 60 characters', max_length=60, null=True, verbose_name='Contact Form button'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='button_form_text_en',
            field=models.CharField(blank=True, default='Contact in a traditional way', help_text='Button scrolls to header section contact info. Max 60 characters', max_length=60, null=True, verbose_name='Contact Form button'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='button_form_text_pl',
            field=models.CharField(blank=True, default='Contact in a traditional way', help_text='Button scrolls to header section contact info. Max 60 characters', max_length=60, null=True, verbose_name='Contact Form button'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='footer_title',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='footer_title_de',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='footer_title_en',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='footer_title_pl',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_description_de',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_description_en',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_description_pl',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_title_de',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_title_en',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meta_title_pl',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='block_id',
            field=models.SlugField(blank=True, help_text='For scroll navigation. ID is created automatically based on header. Keep unique, max 20 characters', max_length=20, null=True, verbose_name='Block ID'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_1_text',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_1_text_de',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_1_text_en',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_1_text_pl',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_2_text',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_2_text_de',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_2_text_en',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='button_2_text_pl',
            field=models.CharField(blank=True, help_text='Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='video_caption',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='video_caption_de',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='video_caption_en',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='video_caption_pl',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='contentblockimage',
            name='caption',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='contentblockimage',
            name='caption_de',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='contentblockimage',
            name='caption_en',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='contentblockimage',
            name='caption_pl',
            field=models.CharField(blank=True, help_text='Max 240 characters', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='externallink',
            name='link_text',
            field=models.CharField(blank=True, help_text='First link is displayed in the header as a button. Max 60 characters', max_length=60, null=True, verbose_name='Link text'),
        ),
        migrations.AlterField(
            model_name='externallink',
            name='link_text_de',
            field=models.CharField(blank=True, help_text='First link is displayed in the header as a button. Max 60 characters', max_length=60, null=True, verbose_name='Link text'),
        ),
        migrations.AlterField(
            model_name='externallink',
            name='link_text_en',
            field=models.CharField(blank=True, help_text='First link is displayed in the header as a button. Max 60 characters', max_length=60, null=True, verbose_name='Link text'),
        ),
        migrations.AlterField(
            model_name='externallink',
            name='link_text_pl',
            field=models.CharField(blank=True, help_text='First link is displayed in the header as a button. Max 60 characters', max_length=60, null=True, verbose_name='Link text'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_description_de',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_description_en',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_description_pl',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_title_de',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_title_en',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='meta_title_pl',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_1_text',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_1_text_de',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_1_text_en',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_1_text_pl',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 1 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_2_text',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_2_text_de',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_2_text_en',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='button_2_text_pl',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button 2 text'),
        ),
        migrations.AlterField(
            model_name='page',
            name='footer_title',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='footer_title_de',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='footer_title_en',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='footer_title_pl',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_description_de',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_description_en',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_description_pl',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_title_de',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_title_en',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_title_pl',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(help_text='URL is created automatically based on menu title. Dont touch unless title is long and not suitable for url. Max 50 characters', unique=True, verbose_name='URL Settings'),
        ),
        migrations.AlterField(
            model_name='page',
            name='thumbnail_caption',
            field=models.CharField(blank=True, help_text='Thumbnail caption as displayed in Section Pages List. Can be left blank for Parent pages. Max 120 characters', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='thumbnail_caption_de',
            field=models.CharField(blank=True, help_text='Thumbnail caption as displayed in Section Pages List. Can be left blank for Parent pages. Max 120 characters', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='thumbnail_caption_en',
            field=models.CharField(blank=True, help_text='Thumbnail caption as displayed in Section Pages List. Can be left blank for Parent pages. Max 120 characters', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='thumbnail_caption_pl',
            field=models.CharField(blank=True, help_text='Thumbnail caption as displayed in Section Pages List. Can be left blank for Parent pages. Max 120 characters', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='link_text',
            field=models.CharField(blank=True, help_text='404 link text, max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='link_text_de',
            field=models.CharField(blank=True, help_text='404 link text, max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='link_text_en',
            field=models.CharField(blank=True, help_text='404 link text, max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='link_text_pl',
            field=models.CharField(blank=True, help_text='404 link text, max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='text',
            field=models.CharField(blank=True, help_text='404 message text, max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='text_de',
            field=models.CharField(blank=True, help_text='404 message text, max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='text_en',
            field=models.CharField(blank=True, help_text='404 message text, max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pagenotfound',
            name='text_pl',
            field=models.CharField(blank=True, help_text='404 message text, max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='accept_button',
            field=models.CharField(blank=True, help_text='Cookies notification "Accept" button text, max 20 characters', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='accept_button_de',
            field=models.CharField(blank=True, help_text='Cookies notification "Accept" button text, max 20 characters', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='accept_button_en',
            field=models.CharField(blank=True, help_text='Cookies notification "Accept" button text, max 20 characters', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='accept_button_pl',
            field=models.CharField(blank=True, help_text='Cookies notification "Accept" button text, max 20 characters', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='cookie_consent',
            field=models.TextField(blank=True, help_text='Cookies notification text, max 500 characters', max_length=500, null=True, verbose_name='Cookies Consent Text'),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='cookie_consent_de',
            field=models.TextField(blank=True, help_text='Cookies notification text, max 500 characters', max_length=500, null=True, verbose_name='Cookies Consent Text'),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='cookie_consent_en',
            field=models.TextField(blank=True, help_text='Cookies notification text, max 500 characters', max_length=500, null=True, verbose_name='Cookies Consent Text'),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='cookie_consent_pl',
            field=models.TextField(blank=True, help_text='Cookies notification text, max 500 characters', max_length=500, null=True, verbose_name='Cookies Consent Text'),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='footer_title',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='footer_title_de',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='footer_title_en',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='footer_title_pl',
            field=models.CharField(blank=True, help_text='Page title as displayed in footer (optional override of menu title), max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_description_de',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_description_en',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_description_pl',
            field=models.TextField(blank=True, help_text='Page description for search results (optional), max 255 characters', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_title_de',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_title_en',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='meta_title_pl',
            field=models.CharField(blank=True, help_text='Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicybutton',
            name='button_text',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button text'),
        ),
        migrations.AlterField(
            model_name='privacypolicybutton',
            name='button_text_de',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button text'),
        ),
        migrations.AlterField(
            model_name='privacypolicybutton',
            name='button_text_en',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button text'),
        ),
        migrations.AlterField(
            model_name='privacypolicybutton',
            name='button_text_pl',
            field=models.CharField(blank=True, help_text='Max 60 characters', max_length=60, null=True, verbose_name='Button text'),
        ),
    ]
