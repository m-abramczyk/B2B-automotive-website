import os
from django.db import models

from labels.models import Label


def upload_to_clients(instance, filename):
    return f'clients/{filename}'

def upload_to_founders(instance, filename):
    return f'team/founders/{filename}'

def upload_to_specialists(instance, filename):
    return f'team/specialists/{filename}'

def upload_to_timeline(instance, filename):
    return f'timeline/{filename}'


#//////////////////////////////////////////////////////////////
# Clients

class Clients(models.Model):

    header = models.CharField(
        blank=True, 
        null=True,
        max_length=120,
    )

    # Button
    button_clients_text = models.CharField(
        ('Clients button text'),
        max_length=60,
        blank=True,
        null=True,
        help_text=('Fill-in if appending Clients list to this block'),
    )
    button_clients_url = models.CharField(
        ('Clients button URL'),
        max_length=255,
        null=True,
        blank=True,
        help_text=('For internal URL skip the language code. Start and end with a trailing slash "/"'),
    )
    new_tab_clients = models.BooleanField(
        ('Open in new tab'),
        default=False,
    )

    # SVG Instructions
    svg_instructions = models.TextField(
        ('SVG Instructions'),
        blank=True,
        null=True,
        help_text="Instructions for uploading SVG files. This text doesn't disaplay on page.",
    )

    class Meta:
        verbose_name = ('Clients')
        verbose_name_plural = ('Clients')

    def __str__(self):
        return 'Clients'


# Clients Images Inline

class ClientLogo(models.Model):
    clients = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
        related_name="logos",
    )
    svg_file = models.FileField(
        upload_to=upload_to_clients,
        help_text=('Upload SVG file (preferably) or PNG if must be'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('Logo')
        verbose_name_plural = ('Logos')
        ordering = ['order']

    def __str__(self):
        return os.path.basename(self.svg_file.name)


#//////////////////////////////////////////////////////////////
# Founders

class Founders(models.Model):

    header = models.CharField(
        blank=True, 
        null=True,
        max_length=120,
    )

    class Meta:
        verbose_name = ('Founders')
        verbose_name_plural = ('Founders')

    def __str__(self):
        return 'Founders'


# Founders Inline

class FounderInfo(models.Model):
    founders = models.ForeignKey(
        Founders,
        on_delete=models.CASCADE,
        related_name="founders",
    )

    name = models.CharField(
        ('Name and surname'),
        max_length=60,
    )
    role = models.TextField(
        max_length=120,
        blank=True,
        null=True,
        help_text=('Founder role. Format text with break-lines, max 60 characters'),
    )
    thumbnail = models.ImageField(
        upload_to=upload_to_founders,
        blank=True,
        null=True,
        help_text=('Portrait, 1:1 ratio, 600px x 600px'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('Founder')
        verbose_name_plural = ('Founders')
        ordering = ['order']

    def __str__(self):
        return (self.name)


#//////////////////////////////////////////////////////////////
# Specialists

class Specialists(models.Model):

    header = models.CharField(
        blank=True, 
        null=True,
        max_length=120,
    )

    class Meta:
        verbose_name = ('Specialists')
        verbose_name_plural = ('Specialists')

    def __str__(self):
        return 'Specialists'


# Specialists Inline

class SpecialistInfo(models.Model):
    specialists = models.ForeignKey(
        Specialists,
        on_delete=models.CASCADE,
        related_name="specialists",
    )

    name = models.CharField(
        ('Name and surname'),
        max_length=60,
    )
    role = models.TextField(
        max_length=120,
        blank=True,
        null=True,
        help_text=('Specialist role. Format text with break-lines, max 60 characters'),
    )
    thumbnail = models.ImageField(
        upload_to=upload_to_specialists,
        blank=True,
        null=True,
        help_text=('Portrait, 1:1 ratio, 600px x 600px'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = ('Specialist')
        verbose_name_plural = ('Specialists')
        ordering = ['order']

    def __str__(self):
        return (self.name)


#//////////////////////////////////////////////////////////////
# Timeline

class Timeline(models.Model):

    header = models.CharField(
        max_length=80,
        help_text=('Block header (required), max 80 characters.'),
    )
    label = models.ForeignKey(
        Label, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        help_text=('Choose or create a new label. Labels are reusable accross the page')
    )

    class Meta:
        verbose_name = ('Timeline')
        verbose_name_plural = ('Timeline')

    def __str__(self):
        return 'Timeline'

# Timeline Image

class TimelineImage(models.Model):
    timeline = models.ForeignKey(
        Timeline,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to=upload_to_timeline,
        help_text=('WEBP / JPG / PNG / GIF / ratio: 3:2 / width: 1500px'),
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    caption = models.CharField(
        max_length=240,
        blank=True,
        null=True,
    )
    long_caption = models.TextField(
        max_length=600,
        blank=True,
        null=True,
    )
    year = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text=('Year / date, for example "2022" or "Ferbruary 2025"'),
    )

    class Meta:
        verbose_name = ('Timeline Image')
        verbose_name_plural = ('Timeline Images')
        ordering = ['order']

    def __str__(self):
        return os.path.basename(self.image.name)