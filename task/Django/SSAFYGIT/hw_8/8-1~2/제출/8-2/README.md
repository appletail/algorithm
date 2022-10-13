- requirements.txt
```txt
asgiref==3.4.1
Django==3.2.9
django-appconf==1.0.5
django-imagekit==4.1.0
pilkit==2.0
Pillow==9.2.0
pytz==2021.3
six==1.16.0
sqlparse==0.4.2
```

- models.py
```py
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
```