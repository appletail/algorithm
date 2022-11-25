# url.py
```py
from django.contrib import admin
from django.urls import path
from prices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('price/<str:thing>/<int:cnt>/', views.product),
    
]
```

# views.py
```py
from django.shortcuts import render

# Create your views here.
def product(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    price = product_price.get(thing)
    context = {
        'product': product_price,
        'thing': thing,
        'price': price,
        'cnt': cnt,
    }
    return render(request, 'price.html', context)
```

# price.html
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
    {% if thing in product %}
        {{ thing }} {{ cnt }}개의 가격은 {% widthratio price 1 cnt %}원 입니다.
    {% else %}
        {{ thing }}은/는 없어용    
    {% endif %}
</body>
</html>
```