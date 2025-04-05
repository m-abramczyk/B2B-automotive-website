from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Label


class LabelAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            "fields": ("label_text", "label_url", "color"),
        }),
    )
    list_display = ("label_text", "color")
    list_editable = ("color",)
    ordering = ("label_text",)


admin.site.register(Label, LabelAdmin)

