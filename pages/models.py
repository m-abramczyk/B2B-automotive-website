import os
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db import models

from covers.models import Cover


def upload_to(instance, filename):
    return f'pages/{instance.slug}/{filename}'


#//////////////////////////////////////////////////////////////
# Home Page

class HomePage(models.Model):
    cover = models.ManyToManyField(Cover, related_name='home_page')
    slug = 'home'

    title = models.TextField(
        max_length=60,
        help_text=('Page title as displayed in page header, max 60 characters'),
    )
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. Auto-filled from menu title'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional)'),
    )

    class Meta:
        verbose_name = ('Home Page')
        verbose_name_plural = ('Home Page')

    def __str__(self):
        return 'Home Page'


#//////////////////////////////////////////////////////////////
# General Page

class Page(models.Model):
    cover = models.ManyToManyField(Cover, related_name='page')

    # Navigation Flags
    is_published = models.BooleanField(
        ('Published'),
        default=False,
        help_text=('Check to publish. Unpublished page doesnt appear in the navigation, but can still be previewed under its URL ([slug] or [parent_slug/slug])'),
    )
    is_section_1_parent = models.BooleanField(
        ('Section 1 Parent'),
        default=False,
        help_text=('Select a single section 1 parent page'),
    )
    is_section_2_parent = models.BooleanField(
        ('Section 2 Parent'),
        default=False,
        help_text=('Select a single section 2 parent page'),
    )
    is_case_studies_index = models.BooleanField(
        ('Case Studies Index'),
        default=False,
        help_text=('Select a single Case Studies Index page'),
    )

    # Hierarchical relationship
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        help_text=('Chose parent page (chose if page belongs to section 1 or 2)'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    # URL and titles
    slug = models.SlugField(
        ('URL Settings'),
        max_length=50,
        unique=True,
        help_text=('URL is created automatically based on menu title. Dont touch unless title is long and not suitable for url'),
    )
    menu_title = models.CharField(
        max_length=60,
        help_text=('Page title as displayed in page menu, max 60 characters'),
    )
    footer_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Page title as displayed in footer (optional override of menu title)'),
    )
    title = models.TextField(
        max_length=60,
        help_text=('Page title as displayed in page header, max 60 characters'),
    )

    # Thumbnail
    thumbnail = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        help_text=('1:1 ratio, 300px x 300px'),
    )
    thumbnail_caption = models.CharField(
        max_length=120,
        default='Thumbnail caption for this page',
        blank=True,
        null=True,
        help_text=('Thumbnail caption as displayed in section pages list'),
    )

    # Section children list
    has_section_pages_list = models.BooleanField(
        ('Display section pages'),
        default=False,
        help_text=('Check to display thumbnails of section pages as the first block below the header (only applicable for section parents)'),
    )
    button_1_text = models.CharField(
        ('Button 1 text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Button text'),
    )
    button_1_url = models.CharField(
        ('Button 1 URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Button URL. For internal URL skip the language code. Start and end with a trailing slash "/"'),
    )
    button_2_text = models.CharField(
        ('Button 1 text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Button text'),
    )
    button_2_url = models.CharField(
        ('Button 1 URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Button URL. For internal URL skip the language code. Start and end with a trailing slash "/"'),
    )

    # Meta data
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. Auto-filled from menu title'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional)'),
    )

    class Meta:
        verbose_name = ('General Page')
        verbose_name_plural = ('General Pages')
        unique_together = ('parent', 'slug')
        ordering = ('order',)

    def __str__(self):
        return (self.menu_title)

    # Ensure only one object is section parent or case studies index
    def clean(self):
        if self.is_section_1_parent and Page.objects.exclude(pk=self.pk).filter(is_section_1_parent=True).exists():
            raise ValidationError("Only one page can be the parent for Section 1.")

        if self.is_section_2_parent and Page.objects.exclude(pk=self.pk).filter(is_section_2_parent=True).exists():
            raise ValidationError("Only one page can be the parent for Section 2.")
        
        if self.is_case_studies_index and Page.objects.exclude(pk=self.pk).filter(is_case_studies_index=True).exists():
            raise ValidationError("Only one page can be the Case Studies Index.")
        
        # Prevent section parents from having a parent
        if (self.is_section_1_parent or self.is_section_2_parent) and self.parent:
            raise ValidationError("Section parent pages cannot have a parent.")
        
    def get_absolute_url(self):
        if self.parent:
            return f"{self.parent.get_absolute_url()}{self.slug}/"
        else:
            return f"/{self.slug}/"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

#//////////////////////////////////////////////////////////////
# Contact

class Contact(models.Model):
    slug = 'contact'

    # URL and titles
    menu_title = models.CharField(
        max_length=60,
        help_text=('Page title as displayed in page menu, max 60 characters'),
    )
    footer_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Page title as displayed in footer (optional override of menu title)'),
    )
    title = models.TextField(
        max_length=60,
        help_text=('Page title as displayed in page header, max 60 characters'),
    )

    # Contact Data
    phone_number = models.CharField(
        max_length=50,
        blank=True,
        help_text=('Phone number in proper format'),
    )
    email = models.CharField(
        max_length=50,
        blank=True,
        help_text=('Email address in proper format'),
    )
    address = models.TextField(
        blank=True,
        help_text=('Address as displayed in header. Format text with break-lines'),
    )
    fiscal_data = models.TextField(
        blank=True,
        help_text=('VAT ID / REGON / KRS as displayed in header. Format text with break-lines'),
    )
    address_footer = models.TextField(
        blank=True,
        help_text=('Address as displayed in footer. Format text with break-lines'),
    )

    # Meta data
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. Auto-filled from menu title'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional)'),
    )

    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contact')

    def __str__(self):
        return 'Contact'
    
    def get_absolute_url(self):
        return reverse('contact')
    

#//////////////////////////////////////////////////////////////
# Contact External Links Inline

class ExternalLink(models.Model):
    page = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        verbose_name = ('Social Link')
    )
    link_text = models.CharField(
        ('Link text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Link text'),
    )
    link_url = models.CharField(
        ('Link URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Link URL'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        help_text=('First link is displayed in the header as a button'),
    )

    class Meta:
        verbose_name = ('External Link')
        verbose_name_plural = ('External Links')
        ordering = ('order',)

    def __str__(self):
        return self.link_text or "Link"
    
#//////////////////////////////////////////////////////////////
# Privacy Policy

class PrivacyPolicy(models.Model):

    is_published = models.BooleanField(
        ('Published'),
        default=False,
        help_text=('Check to publish. Unpublished page doesnt appear in the navigation, but can still be previewed under its URL ([slug] or [parent_slug/slug])'),
    )

    # URL and Titles
    menu_title = models.CharField(
        max_length=60,
        help_text=('Page title as displayed in page menu, max 60 characters'),
    )
    footer_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Page title as displayed in footer (optional override of menu title)'),
    )
    title = models.TextField(
        max_length=60,
        help_text=('Page title as displayed in page header, max 60 characters'),
    )

    text = models.TextField(
        blank=True,
        null=True,
    )

    # Meta data
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. Auto-filled from menu title'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional)'),
    )

    class Meta:
        verbose_name = ('Privacy Policy')
        verbose_name_plural = ('Privacy Policy')

    def __str__(self):
        return (self.menu_title)
    
    def get_absolute_url(self):
        return reverse('privacy_policy')


#//////////////////////////////////////////////////////////////
# Privacy Policy Buttons Inline

class PrivacyPolicyButton(models.Model):
    page = models.ForeignKey(
        PrivacyPolicy,
        on_delete=models.CASCADE,
        verbose_name = ('Privacy Policy Button')
    )
    button_text = models.CharField(
        ('Button text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Button text'),
    )
    button_url = models.CharField(
        ('Button URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('button URL'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('Button')
        verbose_name_plural = ('Buttons')
        ordering = ('order',)

    def __str__(self):
        return self.button_text or "Button"


#//////////////////////////////////////////////////////////////
# 404 Page

class PageNotFound(models.Model):

    text = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('404 message text'),
    )
    link_text = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('404 link text'),
    )

    class Meta:
        verbose_name = ('404 Page')
        verbose_name_plural = ('404 Page')

    def __str__(self):
        return ('404 Page')