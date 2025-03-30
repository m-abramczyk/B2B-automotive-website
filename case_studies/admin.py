from django.contrib import admin

from .models import CaseStudy


# /////////////////////////////////////////////////////////////
# Case Study Detail

class CaseStudyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_published', 'year', 'menu_title', 'thumbnail', 'cover'),
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
    list_display = ('menu_title', 'year', 'is_published')
    list_editable = ('year', 'is_published')
    ordering = ['-year']
    prepopulated_fields= {
        'slug': ('menu_title',),
        }


admin.site.register(CaseStudy, CaseStudyAdmin)