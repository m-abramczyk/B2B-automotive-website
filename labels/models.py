from django.db import models


# Label
class Label(models.Model):
    COLOR_CHOICES = [
        ('light-grey', 'Light Grey'),
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
        max_length=600,
        unique=True
    )
    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default='light-grey'
    )
    
    def __str__(self):
        return self.label_text
