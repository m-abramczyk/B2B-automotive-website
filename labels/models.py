from django.db import models


# Label
class Label(models.Model):
    COLOR_CHOICES = [
        ('light-grey', 'Light Grey'),
        ('grey', 'Grey'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('dark-yellow', 'Dark Yellow'),
        ('yellow', 'Yellow'),
    ]
    
    label_text = models.CharField(
        max_length=60,
        unique=True
    )
    label_url = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text=('(optional) URL for clickable labels (only on Case Study pages). Use relative paths for internal pages (e.g., /contact/). External links starting with "http" and scroll links starting with "#"'),
    )
    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default='light-grey'
    )
    
    def __str__(self):
        return self.label_text
