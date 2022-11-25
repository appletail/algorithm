
# models.py
```py
from django.db import models

# Create your models here.
class Memo(models.Model):
    summary = models.CharField(max_length=20)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

# forms.py
```py
from django import forms

class MemoForm(forms.Form):
    summary = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'summary',
            }
        )
    )

    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'memo',
                'cols': '50',
                'rows': '5',
            }
        )
    )
    
```


# urls.py
```py
from django.urls import path
from . import views

app_name = 'memos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

# views.py
```py
from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm

# Create your views here.
def index(request):
    memos = Memo.objects.all()
    context = {
        'memos': memos
    }
    return render(request, 'memos/index.html', context)


def create(request):
    if request.method == 'POST':
        summary = request.POST.get('summary')
        memo = request.POST.get('memo')
        memos = Memo(summary=summary, memo=memo)
        memos.save()
        return redirect('memos:detail', memos.pk)
    else:
        form = MemoForm()
    context = {
        'form': form,
    }
    return render(request, 'memos/create.html', context)


def detail(request, pk):
    memo = Memo.objects.get(pk=pk)
    context = {
        'memo': memo,
    }
    return render(request, 'memos/detail.html', context)


def delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')
```

---
# create.html
```html
{% extends 'base.html' %}

{% block content %}
<div>
  <h1><b>CREATE</b></h1>
</div>
  <form action="{% url 'memos:create' %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="제출">
  </form>
  <hr>
  <a href="{% url 'memos:index' %}">[back]</a>


{% endblock content %}
```
---
# detail.html
```html
{% extends 'base.html' %}

{% block content %}
<p>요약: {{ memo.summary }}</p>
<p>메모: {{ memo.memo }}</p>
<p>작성 시각: {{ memo.created_at }}</p>
<p>수정 시각: {{ memo.updated_at }}</p>
<form action="{% url 'memos:delete' memo.pk %}" method="post">
    {% csrf_token %}
    <input type="submit" value="삭제">
</form>
<a href="{% url 'memos:index' %}">[back]</a>
{% endblock content %}
```
---
# index.html
```html
{% extends 'base.html' %}

{% block content %}
<h1><b>Memos</b></h1>

<a href="{% url 'memos:create' %}">메모하기</a>
{% for memo in memos %}
  <ul>
    <li>
      <a href="{% url 'memos:detail' memo.pk %}">{{ memo.summary }}</a>
    </li>
    {{ memo.updated_at }}
  </ul>
  
{% endfor %}

{% endblock content %}
```