
from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

# Create your models here.
class Memo(models.Model):

    summary = models.CharField(max_length=20)
    memo = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        blank = True,
        processors=[Thumbnail(200, 200)],
        format='JPEG',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    