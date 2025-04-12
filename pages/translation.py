from modeltranslation.translator import register, TranslationOptions
from .models import HomePage, Page, Contact, ExternalLink, ContentBlock, ContentBlockImage, PrivacyPolicy, PrivacyPolicyButton, PageNotFound

@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'meta_title',
        'meta_description',
    )

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = (
        'menu_title',
        'footer_title',
        'title',
        'thumbnail_caption',
        'button_1_text',
        'button_2_text',
        'meta_title',
        'meta_description',
    )

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = (
        'menu_title',
        'footer_title',
        'title',
        'address',
        'fiscal_data',
        'address_footer',
        'form_header',
        'form_text',
        'button_form_text',
        'meta_title',
        'meta_description',
    )

@register(ExternalLink)
class ExternalLinkTranslationOptions(TranslationOptions):
    fields = (
        'link_text',
    )

@register(ContentBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    fields = (
        'header',
        'text',
        'button_1_text',
        'button_2_text',
        'video_caption',
    )

@register(ContentBlockImage)
class ContentBlockImageTranslationOptions(TranslationOptions):
    fields = (
        'caption',
    )

@register(PrivacyPolicy)
class PrivacyPolicyTranslationOptions(TranslationOptions):
    fields = (
        'menu_title',
        'footer_title',
        'title',
        'text',
        'cookie_consent',
        'accept_button',
        'meta_title',
        'meta_description',
    )

@register(PrivacyPolicyButton)
class PrivacyPolicyButtonTranslationOptions(TranslationOptions):
    fields = (
        'button_text',
    )

@register(PageNotFound)
class PageNotFoundTranslationOptions(TranslationOptions):
    fields = (
        'text',
        'link_text',
    )