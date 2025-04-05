from django.utils.translation import gettext as _
from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    middle_name = forms.CharField(required=False, widget=forms.HiddenInput) # Honeypot field

    class Meta:
        model = ContactSubmission
        fields = ['name', 'surname', 'email', 'company', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Name*')}),
            'surname': forms.TextInput(attrs={'placeholder': _('Surname')}),
            'email': forms.EmailInput(attrs={'placeholder': _('Your e-mail*')}),
            'company': forms.TextInput(attrs={'placeholder': _('Company')}),
            'message': forms.Textarea(attrs={'placeholder': _('Your message*')}),
        }
        error_messages = {
            'name': {'required': _('Field required')},
            'email': {
                'required': _('Field required'),
                'invalid': _('Incorrect e-mail format'),
            },
            'message': {'required': _('Field required')},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ensure the placeholders are translated correctly
        for field in self.fields.values():
            if field.widget.attrs.get('placeholder'):
                field.widget.attrs['placeholder'] = _(field.widget.attrs['placeholder'])