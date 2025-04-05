from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import ClientLogo, Clients, FounderInfo, Founders, SpecialistInfo, Specialists, TimelineImage, Timeline




#//////////////////////////////////////////////////////////////
# Clients

# Clients Images Inline
class ClientLogoInline(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': ('svg_file', 'order'),
        }),
    )
    model = ClientLogo
    extra = 1
    ordering = ['order']


# Clients
class ClientsAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            'fields': ('header',),
        }),
        ('Button', {
            'classes': ('collapse',),
            'fields': (('button_clients_text', 'button_clients_url', 'new_tab_clients'),),
        }),
        ('SVG Instructions', {
            'classes': ('collapse',),
            'fields': ('svg_instructions',),
        }),
    )
    inlines = [
        ClientLogoInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Clients, ClientsAdmin)


#//////////////////////////////////////////////////////////////
# Founders

# Founders Inline
class FounderInfoInline(TranslationStackedInline):
    fieldsets = (
        (None, {
            'fields': (('name', 'order'),),
        }),
        (None, {
            'fields': ('thumbnail', 'role'),
        }),

    )
    model = FounderInfo
    extra = 1
    ordering = ['order']


# Founders
class FoundersAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            'fields': ('header',),
        }),
    )
    inlines = [
        FounderInfoInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Founders, FoundersAdmin)


#//////////////////////////////////////////////////////////////
# Specialists

# Specialists Inline
class SpecialistInfoInline(TranslationStackedInline):
    fieldsets = (
        (None, {
            'fields': (('name', 'order'),),
        }),
        (None, {
            'fields': ('thumbnail', 'role'),
        }),

    )
    model = SpecialistInfo
    extra = 1
    ordering = ['order']


# Specialists
class SpecialistsAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            'fields': ('header',),
        }),
    )
    inlines = [
        SpecialistInfoInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Specialists, SpecialistsAdmin)


#//////////////////////////////////////////////////////////////
# Timeline

# Timeline Inline
class TimelineImageInline(TranslationStackedInline):
    fieldsets = (
        (None, {
            'fields': ('image', 'order'),
        }),
        ('Captions', {
            'classes': ('collapse',),
            'fields': ('year', 'caption', 'long_caption'),
        }),

    )
    model = TimelineImage
    extra = 1
    ordering = ['order']


# Timeline
class TimelineAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            'fields': ('header', 'label'),
        }),
    )
    inlines = [
        TimelineImageInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Timeline, TimelineAdmin)