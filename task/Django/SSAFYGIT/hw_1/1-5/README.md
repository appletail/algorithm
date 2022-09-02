## urls.py
```py
# project5/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menus/', include('menus.urls')),
]

# menus/urls.py
from django.urls import path
from . import views

app_name = "menus"
urlpatterns = [
    path('food/', views.food, name="food"),
    path('drink/', views.drink, name="drink"),
    path('receipt/', views.receipt, name="receipt"),
]

```
---
## views.py
```py
from django.shortcuts import render

# Create your views here.



def food(request):
    food = ['피자', '치킨', '국밥', '초밥', '민초흑당로제마라탕']
    context = {
        'foods': food,
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    drink = ['cider', 'coke', 'miranda', 'fanta', 'eye of finetree']
    context = {
        'drinks': drink
    }
    return render(request, 'menus/drink.html', context)

def receipt(request):
    food = ['피자', '치킨', '국밥', '초밥', '민초흑당로제마라탕']
    drink = ['cider', 'coke', 'miranda', 'fanta', 'eye of finetree']
    select = request.GET.get('receipt').lower
    context = {
        'foods': food,
        'drinks': drink,
        'select': select,
    }
    return render(request, 'menus/receipt.html', context)
```
---

## base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>주문해주세요!</h1>
  <hr>
  {% block content %}
  
  {% endblock content %}
</body>
</html>
```
---

## food.html
```html
{% extends 'base.html' %}

{% block content %}
  {% for food in foods %}
  <p>{{ food }}</p>
  {% endfor %}
  <form action="{% url 'menus:receipt' %}" method="GET">
    <label for="receipt">주문란 : </label>
    <input type="text" name="receipt" id="receipt">
    <input type="submit" value="주문하기">
  </form>

{% endblock content %}
```
---

## drink.html
```html
{% extends 'base.html' %}

{% block content %}
  {% for drink in drinks %}
  <p>{{ drink|capfirst  }}</p>
  {% endfor %}
  <form action="{% url 'menus:receipt' %}" method="GET">
    <label for="receipt">주문란 : </label>
    <input type="text" name="receipt" id="receipt">
    <input type="submit" value="주문하기">
  </form>

{% endblock content %}
```
---

## recript.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  {% if select in drinks or select in foods %}
  <p>{{ select|capfirst  }} 주문받았습니다!</p>
  {% else %}
    <p>{{ select|capfirst  }}은/는 주문이 불가합니다</p>
  {% endif %}

  
</body>
</html>
```