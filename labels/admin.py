from django.contrib import admin
from .models import Label


class LabelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("label_text", "color"),
        }),
    )
    list_display = ("label_text", "color")
    list_editable = ("color",)
    ordering = ("label_text",)


admin.site.register(Label, LabelAdmin)

