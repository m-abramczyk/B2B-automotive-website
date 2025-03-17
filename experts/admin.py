from django.contrib import admin

from .models import Expert


class ExpertAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Credentials', {
            'fields': ('name', 'role', 'thumbnail'),
        }),
        ('Contact Data', {
            'fields': ('phone_number', 'email'),
        }),
        ('Call to action', {
            'fields': ('header', 'button_text', 'button_url'),
        }),
    )
    list_display = ('name',)
    ordering = ('name',)


admin.site.register(Expert, ExpertAdmin)