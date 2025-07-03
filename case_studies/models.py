import os
from django.urls import reverse
from django.db import models

import uuid
from django.conf import settings

from tinymce.models import HTMLField
from model_clone.models import CloneMixin

from covers.models import CaseStudyCover
from experts.models import Expert
from labels.models import Label


def upload_to(instance, filename):
    return f'case-studies/{instance.slug}/{filename}'


def get_placeholder_image(instance, filename):
    """
    Copies placeholder.jpg from static to media/case-studies/placeholders/
    and returns the relative media path.
    """
    placeholder_path = os.path.join(settings.BASE_DIR, 'static/img/placeholder.jpg')
    
    if os.path.exists(placeholder_path):
        with open(placeholder_path, 'rb') as f:
            unique_id = str(uuid.uuid4())[:8]  # nique suffix for each image instance
            file_name = f'placeholder_{unique_id}.jpg'
            relative_path = os.path.join('case-studies', 'placeholders', file_name)
            absolute_path = os.path.join(settings.MEDIA_ROOT, relative_path)            
            os.makedirs(os.path.dirname(absolute_path), exist_ok=True)            
            with open(absolute_path, 'wb') as out_file:
                out_file.write(f.read())

            return relative_path


#//////////////////////////////////////////////////////////////
# Case Study

class CaseStudy(CloneMixin, models.Model):

    is_published = models.BooleanField(
        ('Published'),
        default=False,
        help_text=('Check to publish. Unpublished Case Study doesnt appear in Case Study Index page, but can still be previewed under its URL (example: /company/case-studies/zeekr-x/).'),
    )
    year = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text=('Year as displayed in index thumbnail caption. Also used for sorting the list'),
    )

    # URL and titles
    menu_title = models.CharField(
        ('Title'),
        max_length=60,
        unique=True,
        help_text=('Case Study title as displayed in page header and breadcrumbs. Must be unique, max 60 characters'),
    )
    slug = models.SlugField(
        ('URL Settings'),
        max_length=50,
        unique=True,
        help_text=('URL is created automatically based on title. Dont touch unless title is long and not suitable for url. Must be unique, max 50 characters'),
    )

    # Thumbnail
    thumbnail = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        help_text=('3:2 ratio, 1280px x 854px'),
    )

    # cover
    cover = models.ForeignKey(
        CaseStudyCover,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=('Chose case study cover (no selection = no cover)'),
    )
    index_cover_slider = models.BooleanField(
        ('Show in Index slider'),
        default=True,
        help_text=('Check to display Cover in header slider on Case Study Index Page'),
    )

    # Key data
    header = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Header of Key Data block, max 60 characters'),
    )
    labels_header = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Header of labels group, max 60 characters'),
    )
    text = HTMLField(
        blank=True,
        null=True,
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
        help_text=('Title displayed in browser tab and search results. This field overrides the default title generated from page title, max 60 characters'),
    )
    meta_description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        help_text=('Page description for search results (optional), max 255 characters'),
    )

    # Clone inlines
    _clone_m2o_or_o2m_fields = [
        'labels',
        'data_items',
        'sections',
    ]
    # Exclude fields from cloning
    _clone_excluded_fields = [
        'is_published',
        'cover',
        'thumbnail',
    ]

    class Meta:
        verbose_name = ('Case Study')
        verbose_name_plural = ('Case Studies')
        ordering = ('-year',)

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            placeholder_relative_path = get_placeholder_image(self, 'placeholder.jpg')
            self.thumbnail = placeholder_relative_path
        super().save(*args, **kwargs)

    def __str__(self):
        return (self.menu_title)

    def get_absolute_url(self):
        from pages.models import Page

        case_studies_index = Page.objects.filter(is_case_studies_index=True, is_published=True).first()
        parent = case_studies_index.parent if case_studies_index.parent else None
        return reverse('case_study_detail', kwargs={
            'parent_slug': parent.slug,
            'slug': self.slug,
        })
    

#//////////////////////////////////////////////////////////////
# Label Inline

class CaseStudyLabel(models.Model):
    page = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name="labels",
    )

    label = models.ForeignKey(
        Label, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        help_text=('Choose or create a new label. Labels are reusable accross the page')
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('Case Study Label')
        verbose_name_plural = ('Case Study Labels')
        ordering = ('order',)

    def __str__(self):
        return "Label"


#//////////////////////////////////////////////////////////////
# Data Inline

class CaseStudyData(models.Model):
    page = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name="data_items",
    )

    data_type = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('( Year / Client / Team / Tools ) Displayed in the first column of Key Data table, max 60 characters'),
    )
    data_content = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Displayed in the second column of Key Data table, max 255 characters'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('Key Data Item')
        verbose_name_plural = ('Key Data Items')
        ordering = ('order',)

    def __str__(self):
        return self.data_type or "Untitled Item"
    
    
#//////////////////////////////////////////////////////////////
# Section Inline

class Section(CloneMixin, models.Model):
    case_study = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name="sections",
    )

    header = models.TextField(
        max_length=120,
        blank=True,
        null=True,
        help_text=('Optional Header to display below section images. Format with break-lines. If both Header and Text fields are left empty, images will flow continuously to next section. Max 120 characters'),
    )
    text = HTMLField(
        blank=True,
        null=True,
        help_text=('Optional text to display below section images. Format with break-lines.'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    # Clone nested inline
    _clone_m2o_or_o2m_fields = [
        'section_images',
    ]

    class Meta:
        verbose_name = ('Section')
        verbose_name_plural = ('Sections')
        ordering = ('order',)

    def __str__(self):
        return self.header or "Untitled Section"
    
    
#//////////////////////////////////////////////////////////////
# Section Image Inline

class SectionImage(CloneMixin, models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="section_images",
    )

    image = models.ImageField(
        upload_to=upload_to,
        help_text=('There can be max 3 images in a section. First two images are small, third image is full width. Format: WEBP / JPG / PNG / GIF / ratio: 3:2 / width: 1680px'),
    )    
    caption = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Optional caption to display below an image, max 255 characters'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        help_text=('Image order within the the block'),
    )

    # Exclude image file from cloning
    _clone_excluded_fields = [
        'image',
    ]

    class Meta:
        verbose_name = ('Image')
        verbose_name_plural = ('Images')
        ordering = ['order']

    # assign placeholder if image missing
    def save(self, *args, **kwargs):
        if not self.image:
            placeholder_relative_path = get_placeholder_image(self, 'placeholder.jpg')
            self.image = placeholder_relative_path
        super().save(*args, **kwargs)

    def __str__(self):
        return os.path.basename(self.image.name)
    
    @property
    def slug(self):
        return self.section.case_study.slug