from django.contrib import admin
from .models import Cover, CaseStudyCover


# Covers
class CoverAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cover Video', {
            'classes': ('collapse',),
            'fields': ('cover_video',),
        }),
        ('Cover Image', {
            'fields': ('cover_desktop', 'cover_laptop', 'cover_tablet', 'cover_mobile'),
        }),
    )

admin.site.register(Cover, CoverAdmin)


# Case Study Covers
class CaseStudyCoverAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cover Video', {
            'classes': ('collapse',),
            'fields': ('cover_video',),
        }),
        ('Cover Image', {
            'fields': ('cover_desktop', 'cover_laptop', 'cover_tablet', 'cover_mobile'),
        }),
    )

admin.site.register(CaseStudyCover, CaseStudyCoverAdmin)
