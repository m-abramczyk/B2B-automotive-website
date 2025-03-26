from django.contrib import admin

from .models import ClientLogo, Clients, FounderInfo, Founders, SpecialistInfo, Specialists
# , TimelineImage, Timeline




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
class ClientsAdmin(admin.ModelAdmin):
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
class FounderInfoInline(admin.StackedInline):
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
class FoundersAdmin(admin.ModelAdmin):
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
class SpecialistInfoInline(admin.StackedInline):
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
class SpecialistsAdmin(admin.ModelAdmin):
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