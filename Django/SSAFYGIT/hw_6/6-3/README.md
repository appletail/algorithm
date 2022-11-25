# urls.py
```py
from django.urls import path
from . import views

app_name = 'travels'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

# views.py
```py
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import TravelForm
from .models import Travel
from django.views.decorators.http import require_safe, require_http_methods, require_POST

# Create your views here.
@require_safe
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels': travels,
    }
    return render(request, 'travels/index.html', context)

@require_http_methods(['GET', 'POST'])
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

@require_safe
def detail(request, pk):
    travel = Travel.objects.get(pk=pk)
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)

@require_POST
def delete(request, pk):
    travel = Travel.objects.get(pk=pk)
    travel.delete()
    return redirect('travels:index')

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    travel = Travel.objects.get(pk=pk)
    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelForm(instance=travel)
    context = {
        'form': form,
        'travel': travel,
    }
    return render(request, 'travels/update.html', context)
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
  <form action="{% url 'travels:delete' travel.pk %}" method="post">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'travels:update' travel.pk %}">[UPDATE]</a>
  <hr>
  <a href="{% url 'travels:index' %}">[back]</a>
{% endblock content %}
```