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

- settings.py
```py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR/ 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
```

- base.html
```html
{% load static %}
    <img src="{% static 'images/unknown.png' %}" alt="sky">
```

- models.py
```py
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
        options={'quality':90},
    )
    start_date = models.DateField()
    end_date = models.DateField()
```

- urls.py
```py

```


- views.py
```py
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid:
            travel = form.save()
            return redirect("travels:detail", travel.pk)
    else:
        form = TravelForm()
    context = {"form": form}
    return render(request, "travels/create.html", context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES, instance=travel)
        if form.is_valid:
            form.save()
            return redirect("travels:detail", travel.pk)
    else:
        form = TravelForm(instance=travel)
    context = {
        "travel": travel,
        "form": form,
    }
    return render(request, "travels/update.html", context)
```

- create.html / update.html
```html
  <form action="{% url 'travels:create' %}" method="POST", enctype="multipart/form-data">

<!-- 인코딩타입 추가 -->
```

- index.html
```html
  {% for travel in travels %}
    <img src="{{ travel.image_thumbnail.url }}" alt="{{ travel.image_thumbnail }}">
    <p>장소 : {{ travel.location }}</p>
```

- detail.html
```html
