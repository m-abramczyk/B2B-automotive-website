from django.contrib import admin

from .models import CaseStudy


# /////////////////////////////////////////////////////////////
# Case Study Detail

class CaseStudyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_published', 'order'),
        }),
        ('Thumbnail', {
            'fields': ('thumbnail',),
        }),
        ('Title', {
            'fields': ('menu_title',),
        }),
        ('URL', {
            'classes': ('collapse',),
            'fields': ('slug',),
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
    list_display = ('menu_title', 'order', 'is_published')
    list_editable = ('order', 'is_published')
    ordering = ['order']
    prepopulated_fields= {
        'slug': ('menu_title',),
        }


admin.site.register(CaseStudy, CaseStudyAdmin)