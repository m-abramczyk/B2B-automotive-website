# import nested_admin
# from nested_admin import NestedTabularInline, NestedModelAdmin, SortableHiddenMixin
from django.contrib import admin

from .models import HomePage, Page, Contact, ExternalLink, PrivacyPolicy, PrivacyPolicyButton, PageNotFound


# /////////////////////////////////////////////////////////////
# Cover Inlines

class CoverHomePageInline(admin.TabularInline):
    model = HomePage.cover.through
    max_num = 1
    verbose_name  = 'Cover'
    verbose_name_plural  = 'Cover'

class CoverPageInline(admin.TabularInline):
    model = Page.cover.through
    max_num = 1
    verbose_name  = 'Cover'
    verbose_name_plural  = 'Cover'


# /////////////////////////////////////////////////////////////
# Home Page

class HomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
        ('Meta Data', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )
    inlines = [
        CoverHomePageInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

# /////////////////////////////////////////////////////////////
# General Pages

class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_published',),
        }),
        ('Navigation', {
            'fields': ('is_section_1_parent', 'is_section_2_parent', 'is_case_studies_index', 'parent', 'order'),
        }),
        ('Thumbnail', {
            'fields': ('thumbnail',),
        }),
        ('Title', {
            'fields': ('menu_title', 'footer_title', 'title'),
        }),
        ('URL', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
        ('Meta Data', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )
    list_display = ('menu_title', 'is_section_1_parent', 'is_section_2_parent', 'is_case_studies_index', 'parent', 'order', 'is_published')
    list_editable = ('is_section_1_parent', 'is_section_2_parent', 'is_case_studies_index', 'parent', 'order', 'is_published')
    prepopulated_fields= {
        'slug': ('menu_title',),
        }
    inlines = [
        CoverPageInline,
    ]

    # Restrict the parent choices to Section 1 and Section 2 parents
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs["queryset"] = Page.objects.filter(is_section_1_parent=True) | Page.objects.filter(is_section_2_parent=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# /////////////////////////////////////////////////////////////
# Contact External Link Inline

class ExternalLinkInline(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': ('link_text', 'link_url', 'order'),
        }),
    )
    model = ExternalLink
    extra = 1
    max_num = 3


# /////////////////////////////////////////////////////////////
# Contact

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title', {
            'fields': ('menu_title', 'footer_title', 'title'),
        }),
        ('Contact Data', {
            'fields': ('phone_number', 'email', 'address', 'fiscal_data', 'address_footer'),
        }),
        ('Meta Data', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )
    inlines = [
        ExternalLinkInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


# /////////////////////////////////////////////////////////////
# Privacy Policy Button Inline

class PrivacyPolicyButtonInline(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': ('button_text', 'button_url', 'order'),
        }),
    )
    model = PrivacyPolicyButton
    extra = 1
    max_num = 3


# /////////////////////////////////////////////////////////////
# Privacy Policy

class PrivacyPolicyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_published',),
        }),
        ('Title', {
            'fields': ('menu_title', 'footer_title', 'title'),
        }),
        ('None', {
            'fields': ('text',),
        }),
        ('Meta Data', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )
    list_display = ('menu_title', 'is_published')
    list_editable = ('is_published',)
    inlines = [
        PrivacyPolicyButtonInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

# /////////////////////////////////////////////////////////////
# 404 Page

class PageNotFoundAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('text', 'link_text'),
        }),
    )

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(PageNotFound, PageNotFoundAdmin)