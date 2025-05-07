from django.contrib import admin
from django.contrib import messages
from nested_admin import NestedStackedInline, NestedModelAdmin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from model_clone.admin import CloneModelAdmin

from .models import CaseStudy, CaseStudyLabel, CaseStudyData, Section, SectionImage



# /////////////////////////////////////////////////////////////
# Inlines


# Key Data Inline
class CaseStudyDataInline(TranslationStackedInline):
    fieldsets = (
        (None, {
            'fields': ('data_type', 'data_content', 'order'),
        }),
    )
    model = CaseStudyData
    extra = 0
    ordering = ['order']
    sortable_options = {'disabled': True,}


# Labels Inline
class CaseStudyLabelInline(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': ('label', 'order'),
        }),
    )
    model = CaseStudyLabel
    extra = 0
    ordering = ['order']
    sortable_options = {'disabled': True,}


# Content Block Image Inline
class SectionImageInline(NestedStackedInline, TranslationStackedInline):
    fieldsets = (
        (None, {
            'fields': ('image', 'order', 'caption'),
        }),
    )
    model = SectionImage
    extra = 0
    max_num = 3
    ordering = ['order']
    sortable_options = {'disabled': True,}


# Sections Inline
class SectionInline(NestedStackedInline, TranslationStackedInline):
    fieldsets = (
        (None, {
            'fields': ('order', 'header', 'text'),
        }),
    )
    model = Section
    extra = 0
    ordering = ['order']
    sortable_options = {'disabled': True,}
    inlines = [SectionImageInline]


# /////////////////////////////////////////////////////////////
# Case Study Detail

class CaseStudyAdmin(CloneModelAdmin, NestedModelAdmin, TranslationAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_published', 'index_cover_slider', 'year', 'menu_title', 'thumbnail', 'cover'),
        }),
        ('URL', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
        ('Key Data Section', {
            'classes': ('collapse',),
            'fields': ('header', 'labels_header', 'text'),
        }),
        ('Expert', {
            'classes': ('collapse',),
            'fields': ('expert',),
        }),
        ('Meta Data', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )
    list_display = ('menu_title', 'year', 'index_cover_slider', 'is_published')
    list_editable = ('year', 'index_cover_slider', 'is_published')
    ordering = ['-year']
    prepopulated_fields= {
        'slug': ('menu_title',),
        }
    inlines = [
        CaseStudyLabelInline,
        CaseStudyDataInline,
        SectionInline,
    ]

    def save_model(self, request, obj, form, change):
        if '-copy' in obj.slug:
            self.message_user(
                request,
                "Reminder: after cloning, please adjust the slug — it still contains a temporary '-copy' suffix.",
                level=messages.WARNING
            )
        super().save_model(request, obj, form, change)


admin.site.register(CaseStudy, CaseStudyAdmin)