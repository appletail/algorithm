
# models.py
```py
from django.db import models

# Create your models here.
class Travel(models.Model):
    location = models.CharField(max_length=10)
    plan = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
```

# forms.py
```py
from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 제주도',
            }
        )
    )
    
    plan = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'ex) 슉.슈슉.',
            }
        )
    )

    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 2022-02-22',
            }
        )
    )

    end_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 2022-02-22',
            }
        )
    )
    class Meta:
        model = Travel
        fields = '__all__'

```


# urls.py
```py
from django.urls import path
from . import views

app_name = 'travels'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
]
```

# views.py
```py
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import TravelForm
from .models import Travel

# Create your views here.
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels': travels,
    }
    return render(request, 'travels/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelForm()
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = Travel.objects.get(pk=pk)
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)
```

---
# create.html
```html
{% extends 'base.html' %}

{% block content %}
  <h1><b>CREATE</b></h1>
  <form action="{% url 'travels:create' %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="제출">
  </form>
  <hr>
  <a href="{% url 'travels:index' %}">[back]</a>
{% endblock content %}
```
---
# detail.html
```html
{% extends 'base.html' %}

{% block content %}
  <h1><b>DETAIL</b></h1>
  <h1><b>{{ travel.pk }} 번째 글</b></h1>
  <hr>
  <p>장소 : {{ travel.location }}</p>
  <p>계획 : {{ travel.plan }}</p>
  <p>시작일 : {{ travel.start_date }}</p>
  <p>종료일 : {{ travel.end_date }}</p>
  <hr>
  <a href="{% url 'travels:index' %}">[back]</a>
{% endblock content %}
```
---
# index.html
```html
{% extends 'base.html' %}

{% block content %}
  <h1><b>travels</b></h1>
  <a style="text-decoration:none" href="{% url 'travels:create' %}">CREATE</a>
  <hr>
  {% for travel in travels %}
    <p>장소 : {{ travel.location }}</p>
    <p>시작일 : {{ travel.start_date }}</p>
    <a href="{% url 'travels:detail' travel.pk %}">[detail]</a>
    <hr>
  {% endfor %}

{% endblock content %}
```