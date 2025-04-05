from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Expert


class ExpertAdmin(TranslationAdmin):
    fieldsets = (
        ('Credentials', {
            'classes': ('collapse',),
            'fields': ('name', 'role', 'thumbnail'),
        }),
        ('Contact Data', {
            'classes': ('collapse',),
            'fields': ('phone_number', 'email'),
        }),
        ('Call to action', {
            'classes': ('collapse',),
            'fields': ('header', 'label', 'button_text', 'button_url'),
        }),
    )
    list_display = ('name',)
    ordering = ('name',)


admin.site.register(Expert, ExpertAdmin)