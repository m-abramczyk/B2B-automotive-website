from django.contrib import admin
from .models import Cover


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
