import os
from django.urls import reverse
from django.db import models
from tinymce.models import HTMLField

from covers.models import CaseStudyCover
from experts.models import Expert
from labels.models import Label


def upload_to(instance, filename):
    return f'case-studies/{instance.slug}/{filename}'


#//////////////////////////////////////////////////////////////
# Case Study

class CaseStudy(models.Model):

    # Navigation
    is_published = models.BooleanField(
        ('Published'),
        default=False,
        help_text=('Check to publish. Unpublished page doesnt appear in the navigation, but can still be previewed under its URL ([slug] or [parent_slug/slug])'),
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
        help_text=('Page title as displayed in page header and breadcrumbs, max 60 characters'),
    )
    slug = models.SlugField(
        ('URL Settings'),
        max_length=50,
        unique=True,
        help_text=('URL is created automatically based on menu title. Dont touch unless title is long and not suitable for url'),
    )

    # Thumbnail
    thumbnail = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        help_text=('1:1 ratio, 300px x 300px'),
    )

    # cover
    cover = models.ForeignKey(
        CaseStudyCover,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=('Chose case study cover (no selection = no cover)'),
    )

    # Key data
    header = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Header of Key Data block'),
    )
    labels_header = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Header of labels group'),
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
        help_text=('Chose an expert to display at the bottom of the page (no selection = no expert)'),
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
        verbose_name = ('Case Study')
        verbose_name_plural = ('Case Studies')
        ordering = ('-year',)

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
        help_text=('Displayed in the first column of Key Data table'),
    )
    data_content = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=('Displayed in the second column of Key Data table'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('Data Item')
        verbose_name_plural = ('Data Items')
        ordering = ('order',)

    def __str__(self):
        return self.data_type or "Data Item"
    
    
#//////////////////////////////////////////////////////////////
# Section Inline

class Section(models.Model):
    case_study = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name="sections",
    )

    header = models.TextField(
        max_length=120,
        blank=True,
        null=True,
        help_text=('Optional Header to display below section images. Format with break-lines.'),
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

    class Meta:
        verbose_name = ('Section')
        verbose_name_plural = ('Sections')
        ordering = ('order',)

    def __str__(self):
        return self.header or "Untitled Section"
    
    
#//////////////////////////////////////////////////////////////
# Section Image Inline

class SectionImage(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="section_images",
    )

    image = models.ImageField(
        upload_to=upload_to,
        help_text=('WEBP / JPG / PNG / GIF / ratio: 3:2 / width: 1680px'),
    )    
    caption = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        help_text=('Optional caption to display below an image. Format with break-lines.'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )


    class Meta:
        verbose_name = ('Image')
        verbose_name_plural = ('Images')
        ordering = ['order']

    def __str__(self):
        return os.path.basename(self.image.name)
    
    @property
    def slug(self):
        return self.section.case_study.slug