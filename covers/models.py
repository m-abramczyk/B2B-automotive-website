import os
from django.core.validators import FileExtensionValidator

from django.db import models


def upload_to(instance, filename):
    return f'covers/{filename}'

# Covers
class Cover(models.Model):

    # Cover Video
    cover_video = models.FileField(
        upload_to=upload_to,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm'])],
        help_text=('WEBM / MP4 file, recommended max size: 4Mb / length: ~30s. Upload either Video or Image Cover, not both.'),
    )

    # Cover Image
    cover_desktop = models.ImageField(
        upload_to=upload_to,
        blank=True,
        help_text=('Horizontal, approximately 16:9 ratio, ratio 1920px wide'),
    )
    cover_laptop = models.ImageField(
        upload_to=upload_to,
        blank=True,
        help_text=('Horizontal, approximately 16:9 ratio, 1680px wide'),
    )
    cover_tablet = models.ImageField(
        upload_to=upload_to,
        blank=True,
        help_text=('Square or slightly vertical ratio, 1024px wide'),
    )
    cover_mobile = models.ImageField(
        upload_to=upload_to,
        blank=True,
        help_text=('Square or slightly vertical ratio, 768px wide'),
    )


    class Meta:
        verbose_name = ('Cover')
        verbose_name_plural = ('Covers')

    def __str__(self):
        if self.cover_desktop:
            return os.path.basename(self.cover_desktop.name)
        elif self.cover_video:
            return os.path.basename(self.cover_video.name)
        else:
            return super().__str__()