from django.contrib import admin

from .models import Expert


class ExpertAdmin(admin.ModelAdmin):
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