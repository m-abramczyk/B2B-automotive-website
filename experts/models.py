from django.db import models


def upload_to(instance, filename):
    return f'experts/{filename}'

# Expert
class Expert(models.Model):

    # Credentials
    name = models.CharField(
        ('Name and surname'),
        max_length=60,
    )
    role = models.TextField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Expert role. Format text with break-lines, max 60 characters'),
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

    # Call to action
    header = models.TextField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('Call to action header. Format text with break-lines'),
    )
    button_text = models.CharField(
        ('Button text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Button text'),
    )
    button_url = models.CharField(
        ('Button URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('Button URL. For internal URL skip the language code. Start and end with a trailing slash "/"'),
    )

    class Meta:
        verbose_name = ('Expert')
        verbose_name_plural = ('Experts')

    def __str__(self):
        return (self.name)