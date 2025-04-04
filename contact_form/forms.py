from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    middle_name = forms.CharField(required=False, widget=forms.HiddenInput) # Honeypot field

    class Meta:
        model = ContactSubmission
        fields = ['name', 'surname', 'email', 'company', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name*'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Surname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your e-mail*'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message*'}),
        }
        error_messages = {
            'name': {'required': 'Field required'},
            'email': {
                'required': 'Field required',
                'invalid': 'Incorrect e-mail format',
            },
            'message': {'required': 'Field required'},
        }