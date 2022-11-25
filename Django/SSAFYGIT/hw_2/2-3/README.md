# url.py
```py
from django.urls import path
from . import views

app_name = 'throw_catch'
urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
]
```

# views.py
```py
from django.shortcuts import render

# Create your views here.
def first(request):
    catch = request.GET.get('catch')
    context = {
        'catch': catch,
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    catch = request.GET.get('catch')
    context = {
        'catch': catch,
    }
    return render(request, 'throw_catch/second.html', context)
```

# first.html
```html
    {% if catch == None or catch == '' %}
    <p>catch : 아무것도 받지 못함</p>
    {% else %}
    <p>catch : {{ catch }} 을/를 받음!</p>
    {% endif %}
    <form action="{% url 'throw_catch:second' %}" method="get">
        <label for="input">throw: </label>
        <input type="text" name="catch" id="input">
        <input type="submit" value="휙">
    </form>
```

# second.html
```html
    {% if catch == None or catch == '' %}
    <p>catch : 아무것도 받지 못함</p>
    {% else %}
    <p>catch : {{ catch }} 을/를 받음!</p>
    {% endif %}
    <form action="{% url 'throw_catch:first' %}" method="get">
        <label for="input">throw: </label>
        <input type="text" name="catch" id="input">
        <input type="submit" value="휙">
    </form>
```