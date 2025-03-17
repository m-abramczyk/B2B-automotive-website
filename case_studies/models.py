from django.urls import reverse
from django.db import models

from experts.models import Expert


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
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
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
        ordering = ('order',)

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