from django.db import models
from labels.models import Label


def upload_to(instance, filename):
    return f'experts/{filename}'

# Expert
class Expert(models.Model):

    # Credentials
    name = models.CharField(
        ('Name and surname'),
        max_length=60,
        help_text=('Max 60 characters'),
    )
    role = models.TextField(
        max_length=120,
        blank=True,
        null=True,
        help_text=('Expert role. Format text with break-lines, max 120 characters'),
    )
    thumbnail = models.ImageField(
        upload_to=upload_to,        
        blank=True,
        null=True,
        help_text=('Expert thumbnail 1:1 ratio, 600px x 600px'),
    )

    # Contact Data
    phone_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=('Phone number in proper format'),
    )
    email = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=('Email address in proper format'),
    )
    linkedin = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=('Expert Linkedin URL'),
    )

    # Label
    label = models.ForeignKey(
        Label, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        help_text=('Choose or create a new label. Labels are reusable accross the page')
    )

    # Call to action
    header = models.TextField(
        max_length=80,
        blank=True,
        null=True,
        help_text=('Call to action header. Format text with break-lines, max 80 characters'),
    )
    button_text = models.CharField(
        ('Button text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Button text, max 60 characters'),
    )
    button_url = models.CharField(
        ('Button URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Use relative paths for internal pages (e.g., /contact/). External links starting with "http" and scroll links starting with "#"'),
    )

    class Meta:
        verbose_name = ('Expert')
        verbose_name_plural = ('Experts')

    def __str__(self):
        return (self.name)