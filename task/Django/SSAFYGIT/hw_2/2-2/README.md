# url.py
```py
from django.urls import path
from calculators import views

app_name = 'calculators'
urlpatterns = [
    path('calculator/<int:num1>/<int:num2>/', views.calculators),
]

```

# views.py
```py
from django.shortcuts import render

# Create your views here.
def calculators(request, num1, num2):
    if num2 != 0:
        nanugi = num1 / num2
    else:
        nanugi = 0
    context = {
        'num1': num1,
        'num2': num2,
        'num2_minus': -num2,
        'nanugi': nanugi,
    }
    return render(request, 'calculators/calculator.html', context)
```

# calculator.html
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
    <h1><b>계산결과</b></h1>
    <p>{{ num1 }} + {{ num2 }} = {{ num1|add:num2 }} </p>
    <p>{{ num1 }} * {{ num2 }} = {% widthratio num1 1 num2 %} </p>
    <p>{{ num1 }} - {{ num2 }} = {{ num1|add:num2_minus }} </p>
    {% if num2 == 0 %}
    <p>계산할 수 없습니다</p>
    {% else %}
    <p>{{ num1 }} / {{ num2 }} = {{ nanugi }} </p>
    {% endif %}
</body>
</html>
```