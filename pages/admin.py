# import nested_admin
from nested_admin import NestedTabularInline, NestedStackedInline, NestedGenericStackedInline, NestedModelAdmin
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline, GenericInlineModelAdmin

from .models import ContentBlock, ContentBlockImage, HomePage, Page, Contact, ExternalLink, PrivacyPolicy, PrivacyPolicyButton, PageNotFound



# /////////////////////////////////////////////////////////////
# Inlines

# Content Block Image Inline
class ContentBlockImageInline(NestedStackedInline):
    fieldsets = (
        (None, {
            'fields': ('image', 'order', 'caption'),
        }),
    )
    model = ContentBlockImage
    extra = 0
    ordering = ['order']
    sortable_options = {'disabled': True,}


# Content Block Inline
class ContentBlockInline(NestedGenericStackedInline):
    fieldsets = (
        (None, {
            'fields': ('order', 'block_type'),
        }),
        (None, {
            'fields': ('header', 'block_id', 'label', 'text'),
        }),
        (None, {
            'fields': (('button_1_text', 'button_1_url', 'new_tab_1'), ('button_2_text', 'button_2_url', 'new_tab_2')),
        }),
        (None, {
            'fields': ('append_scroll_nav', 'append_clients', 'append_timeline', 'append_founders', 'append_team'),
        }),
        (None, {
            'fields': ('display_type', 'video', 'video_caption'),
        }),
    )
    model = ContentBlock
    extra = 0
    ordering = ['order']
    sortable_options = {'disabled': True,}
    prepopulated_fields= {'block_id': ('header',),}
    inlines = [ContentBlockImageInline]


# Contact External Link Inline
class ExternalLinkInline(admin.StackedInline):
    fieldsets = (
        (None, {
            'fields': ('link_text', 'link_url', 'order'),
        }),
    )
    model = ExternalLink
    extra = 0
    max_num = 3
    ordering = ['order']
    sortable_options = {'disabled': True,}


# Privacy Policy Button Inline
class PrivacyPolicyButtonInline(admin.StackedInline):
    fieldsets = (
        (None, {
            'fields': ('button_text', 'button_url', 'order'),
        }),
    )
    model = PrivacyPolicyButton
    extra = 0
    max_num = 3
    ordering = ['order']


# /////////////////////////////////////////////////////////////
# Home Page

class HomePageAdmin(NestedModelAdmin):
    fieldsets = (
        ('Title', {
            'classes': ('collapse',),
            'fields': ('title',),
        }),
        ('Cover', {
            'classes': ('collapse',),
            'fields': ('cover',),
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
    inlines = [
        ContentBlockInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

# /////////////////////////////////////////////////////////////
# General Pages

class PageAdmin(NestedModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_published',),
        }),
        ('Navigation', {
            'classes': ('collapse',),
            'fields': ('parent', 'order'),
        }),
        ('Cover', {
            'classes': ('collapse',),
            'fields': ('cover',),
        }),
        ('Thumbnail', {
            'classes': ('collapse',),
            'fields': ('thumbnail', 'thumbnail_caption'),
        }),
        ('Title', {
            'classes': ('collapse',),
            'fields': ('menu_title', 'footer_title', 'title'),
        }),
        ('URL', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
        ('Expert', {
            'classes': ('collapse',),
            'fields': ('expert',),
        }),
        ('Section Pages List (For section parent pages)', {
            'classes': ('collapse',),
            'fields': ('has_section_pages_list', 'button_1_text', 'button_1_url', 'button_2_text', 'button_2_url'),
        }),
        ('Meta Data', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )
    list_display = ('display_menu_title', 'is_section_1_parent', 'is_section_2_parent', 'is_case_studies_index', 'parent', 'order', 'is_published')
    list_editable = ('is_section_1_parent', 'is_section_2_parent', 'is_case_studies_index', 'parent', 'order', 'is_published')
    prepopulated_fields= {
        'slug': ('menu_title',),
        }
    inlines = [
        ContentBlockInline,
    ]

    # Append 'index' if is_case_study_index
    def display_menu_title(self, obj):
        return f"{obj.menu_title} index" if obj.is_case_studies_index else obj.menu_title
    display_menu_title.short_description = "Page Title" # Custom column name

    # Restrict the parent choices to Section 1 and Section 2 parents
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs["queryset"] = Page.objects.filter(is_section_1_parent=True) | Page.objects.filter(is_section_2_parent=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# /////////////////////////////////////////////////////////////
# Contact

class ContactAdmin(NestedModelAdmin):
    fieldsets = (
        ('Title', {
            'classes': ('collapse',),
            'fields': ('menu_title', 'footer_title', 'title'),
        }),
        ('Contact Data', {
            'classes': ('collapse',),
            'fields': ('phone_number', 'email', 'address', 'fiscal_data', 'address_footer'),
        }),
        ('Contact Form', {
            'classes': ('collapse',),
            'fields': ('form_header', 'form_text', 'label', 'button_form_text'),
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
    inlines = [
        ExternalLinkInline,
        ContentBlockInline,
    ]

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


# /////////////////////////////////////////////////////////////
# Privacy Policy

class PrivacyPolicyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_published',),
        }),
        ('Title', {
            'classes': ('collapse',),
            'fields': ('menu_title', 'footer_title', 'title'),
        }),
        ('Text', {
            'classes': ('collapse',),
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