from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField

class Travel(models.Model):
    location = models.CharField(max_length=10)
    plan = models.TextField()
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(100, 100)],
        format='JPEG',
        options={'quality': 90},
    )
    start_date = models.DateField()
    end_date = models.DateField()
