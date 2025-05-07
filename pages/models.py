import os
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from tinymce.models import HTMLField

from django.urls import reverse
from django.utils.translation import get_language, override
from django.db import models

from covers.models import Cover
from experts.models import Expert
from labels.models import Label


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

    cover = models.ForeignKey(
        Cover,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=('Chose or add page cover (no selection = no cover)'),
    )

    expert = models.ForeignKey(
        Expert,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=('Chose or add an expert to display at the bottom of the page (no selection = no expert)'),
    )

    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional), max 255 characters'),
    )

    class Meta:
        verbose_name = ('Home Page')
        verbose_name_plural = ('Home Page')

    def __str__(self):
        return 'Home Page'


#//////////////////////////////////////////////////////////////
# General Page

class Page(models.Model):

    # Navigation Flags
    is_published = models.BooleanField(
        ('Published'),
        default=False,
        help_text=('Check to publish. Unpublished page doesnt appear in the navigation, but can still be previewed under its URL (example: /company/ or /company/team/)'),
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
        on_delete=models.SET_NULL,
        help_text=('Chose parent page (chose if page belongs to section 1 or 2)'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        help_text=('Determines the order of subpages in menu and footer. N/A for parent pages (Can be left at "0")'),
    )

    # URL and titles
    slug = models.SlugField(
        ('URL Settings'),
        max_length=50,
        unique=True,
        help_text=('URL is created automatically based on menu title. Dont touch unless title is long and not suitable for url. Max 50 characters'),
    )
    menu_title = models.CharField(
        max_length=60,
        help_text=('Page title as displayed in page menu, max 60 characters'),
    )
    footer_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Page title as displayed in footer (optional override of menu title), max 60 characters'),
    )
    title = models.TextField(
        max_length=60,
        help_text=('Page title as displayed in page header, max 60 characters'),
    )

    # Cover
    cover = models.ForeignKey(
        Cover,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=('Chose or add page cover (no selection = no cover)'),
    )

    # Thumbnail
    thumbnail = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        help_text=('1:1 ratio, 300px x 300px. For display in desktop menu and Section Pages List. Can be left blank for Parent pages.'),
    )
    thumbnail_caption = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        help_text=('Thumbnail caption as displayed in Section Pages List. Can be left blank for Parent pages. Max 120 characters'),
    )

    # Expert
    expert = models.ForeignKey(
        Expert,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=('Chose or add an expert to display at the bottom of the page (no selection = no expert)'),
    )

    # Section children list
    has_section_pages_list = models.BooleanField(
        ('Display section pages'),
        default=False,
        help_text=('Check to display thumbnails of section pages as the first block below the header (only applicable for section Parent pages)'),
    )
    button_1_text = models.CharField(
        ('Button 1 text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Max 60 characters'),
    )
    button_1_url = models.CharField(
        ('Button 1 URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Use relative paths for internal pages (e.g., /contact/). External links starting with "http" and scroll links starting with "#"'),
    )
    button_2_text = models.CharField(
        ('Button 2 text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Max 60 characters'),
    )
    button_2_url = models.CharField(
        ('Button 2 URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Use relative paths for internal pages (e.g., /contact/). External links starting with "http" and scroll links starting with "#"'),
    )

    # Meta data
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional), max 255 characters'),
    )

    class Meta:
        verbose_name = ('General Page')
        verbose_name_plural = ('General Pages')
        unique_together = ('parent', 'slug')
        ordering = ('order',)

    def __str__(self):
        return f"{self.menu_title} index" if self.is_case_studies_index else self.menu_title

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
        
        # Prevent subsections from having a section pages list
        if self.parent and self.has_section_pages_list:
            raise ValidationError("Subsection page cannot have a section pages list.")

        
    def get_full_slug(self):
        """Recursively build the full slug path."""
        if self.parent:
            return f"{self.parent.get_full_slug()}/{self.slug}"
        return self.slug

    def get_absolute_url(self):
        lang = get_language()
        with override(lang):
            return reverse('general_page', kwargs={'slug': self.get_full_slug()})

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
        help_text=('Page title as displayed in footer (optional override of menu title), max 60 characters'),
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
    address_footer = HTMLField(
        blank=True,
        help_text=('Address as displayed in footer. Format text with break-lines. For email link use mailto:email@g3.net.pl'),
    )

    # Contact Form
    form_header = models.CharField(
        ('Contact Form Header'),
        max_length=80,
        blank=True,
        null=True,
        default='Drop us a line:',
        help_text=('Max 80 characters.'),
    )
    form_text = HTMLField(
        ('Contact Form Text'),
        blank=True,
        null=True,
        help_text=('Format with break-lines.'),
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.SET_NULL,
        blank=True, 
        null=True,
        help_text=('Choose or create a new label. Labels are reusable accross the page')
    )
    button_form_text = models.CharField(
        ('Contact Form button'),
        max_length=60,
        blank=True,
        null=True,
        default='Contact in a traditional way',
        help_text=('Button scrolls to header section contact info. Max 60 characters'),
    )

    # Expert
    expert = models.ForeignKey(
        Expert,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=('Chose or add an expert to display at the bottom of the page (no selection = no expert)'),
    )

    # Meta data
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional), max 255 characters'),
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
        help_text=('First link is displayed in the header as a button. Max 60 characters'),
    )
    link_url = models.CharField(
        ('Link URL'),
        max_length=255,
        null=True,
        blank=True,
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('External Link')
        verbose_name_plural = ('External Links')
        ordering = ('order',)

    def __str__(self):
        return self.link_text or "Link"


#//////////////////////////////////////////////////////////////
# Content Block

class ContentBlock(models.Model):
    
    BLOCK_TYPES = [
        ('left', 'Left'),
        ('right', 'Right'),
        ('full-width', 'Full-width'),
    ]

    IMAGE_DISPLAY_TYPES = [
        ('carousel', 'Carousel'),
        ('wipe', 'Wipe'),
    ]

    # Block Settings
    block_type = models.CharField(
        max_length=20,
        choices=BLOCK_TYPES,
        default='left',
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    block_id = models.SlugField(
        ('Block ID'),
        max_length=20,
        blank=True,
        null=True,
        help_text=('For scroll navigation. ID is created automatically based on header. Keep unique, max 20 characters'),
    )

    # Block content
    header = models.CharField(
        max_length=80,
        help_text=('Block header (required), max 80 characters.'),
    )
    text = HTMLField(
        blank=True,
        null=True,
    )

    # Label
    label = models.ForeignKey(
        Label, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        help_text=('Choose or create a new label. Labels are reusable accross the page')
    )

    # Buttons
    button_1_text = models.CharField(
        ('Button 1 text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters'),
    )
    button_1_url = models.CharField(
        ('Button 1 URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Use relative paths for internal pages (e.g., /contact/). External links starting with "http" and scroll links starting with "#"'),
    )
    new_tab_1 = models.BooleanField(
        ('Open in new tab'),
        default=False,
    )

    button_2_text = models.CharField(
        ('Button 2 text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Buttons 1 and 2 are only displayed in Left and Right blocks. Max 60 characters'),
    )
    button_2_url = models.CharField(
        ('Button 2 URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Use relative paths for internal pages (e.g., /contact/). External links starting with "http" and scroll links starting with "#"'),
    )
    new_tab_2 = models.BooleanField(
        ('Open in new tab'),
        default=False,
    )

    # Append block flags
    append_clients = models.BooleanField(
        ('Append Clients list'),
        default=False,
        help_text=('Append Clients list below the block'),
    )
    append_timeline = models.BooleanField(
        ('Append Timeline block'),
        default=False,
        help_text=('Append Timeline block below the block'),
    )
    append_founders = models.BooleanField(
        ('Append Founders list'),
        default=False,
        help_text=('Append Founders list below the block'),
    )
    append_team = models.BooleanField(
        ('Append Key Specialists list'),
        default=False,
        help_text=('Append Key Specialists list below the block'),
    )

    # Carousel Settings
    display_type = models.CharField(
        ('Image Display Type'),
        max_length=20,
        choices=IMAGE_DISPLAY_TYPES,
        default='carousel',
        help_text=('Choose display type for the images. If set to "wipe", the first two images will be used.'),
    )
    video = models.FileField(
        upload_to=upload_to,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm'])],
        help_text=('Overrides Image Display Type: replaces carousel with a single video: WEBM / MP4 file / recommended max size: 4Mb / length: ~30s'),
    )
    video_caption = models.CharField(
        max_length=240,
        blank=True,
        null=True,
        help_text=('Max 240 characters'),
    )

    # Generic relation to support multiple models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = ('Content Block')
        verbose_name_plural = ('Content Blocks')
        ordering = ['order']

    def __str__(self):
        return self.header
    
    @property
    def slug(self):
        return self.content_object.slug


#//////////////////////////////////////////////////////////////
# Content Block Image

class ContentBlockImage(models.Model):
    content_block = models.ForeignKey(
        ContentBlock,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to=upload_to,
        help_text=('WEBP / JPG / PNG / GIF / ratio: 3:2 / width: 1280px (blocks Left, Right) / width: 1680px (block Full-width)'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    caption = models.CharField(
        max_length=240,
        blank=True,
        null=True,
        help_text=('Max 240 characters'),
    )

    class Meta:
        verbose_name = ('Image')
        verbose_name_plural = ('Images')
        ordering = ['order']

    def __str__(self):
        return os.path.basename(self.image.name)
    
    @property
    def slug(self):
        return self.content_block.content_object.slug


#//////////////////////////////////////////////////////////////
# Privacy Policy

class PrivacyPolicy(models.Model):

    is_published = models.BooleanField(
        ('Published'),
        default=False,
        help_text=('Check to publish. Unpublished page doesnt appear in the navigation, but can still be previewed under its URL (example: /company/ or /company/team/)'),
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
        help_text=('Page title as displayed in footer (optional override of menu title), max 60 characters'),
    )
    title = models.TextField(
        max_length=60,
        help_text=('Page title as displayed in page header, max 60 characters'),
    )

    text = HTMLField(
        blank=True,
        null=True,
    )

    # Cookies Modal
    cookie_consent = models.TextField(
        ('Cookies Consent Text'),
        max_length=500,
        blank=True,
        null=True,
        help_text=('Cookies notification text, max 500 characters'),
    )
    accept_button = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text=('Cookies notification "Accept" button text, max 20 characters'),
    )

    # Meta data
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Title displayed in browser tab and search results. This field overrides the default title generated from page title. Max 60 characters'),
    )
    meta_description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional), max 255 characters'),
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
        help_text=('Max 60 characters'),
    )
    button_url = models.CharField(
        ('Button URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Use relative paths for internal pages (e.g., /contact/). External links starting with "http" and scroll links starting with "#"'),
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
        help_text=('404 message text, max 255 characters'),
    )
    link_text = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('404 link text, max 60 characters'),
    )

    class Meta:
        verbose_name = ('404 Page')
        verbose_name_plural = ('404 Page')

    def __str__(self):
        return ('404 Page')