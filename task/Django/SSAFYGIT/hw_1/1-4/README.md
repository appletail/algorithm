## first.html
  <p>catch! I catch {{ third_catch }}!</p>
  <form action="/second/" method="GET">
    <p>throw! <input type="text" name="first"> <input type="submit" value="획"> </p>
  </form>

## second.html
  <p>catch! I catch {{ first_catch }}!</p>
  <form action="/third/" method="GET">
    <p>and throw! <input type="text" name="first"> twice! <input type="text" name="second"> <input type="submit" value="획"> </p>
  </form>

## third.html
  <p>oops! I catch only {{ catch|random }} ㅠㅠ</p>
  <form action="/first/" method="GET">
  <p>throw! <input type="text" name="third"><input type="submit" value="획"></p>
  </form>

## views.py
```py
def first(request):
    third_catch = request.GET.get('third', 'nothing')
    context = {
        'third_catch': third_catch
    }
    return render(request, 'first.html', context)

def second(request):
    first_catch = request.GET.get('first')
    context = {
        'first_catch': first_catch
    }
    return render(request, 'second.html', context)
    
def third(request):
    first_catch = request.GET.get('first')
    second_catch = request.GET.get('second')
    catch = [first_catch, second_catch]
    context = {
        'catch': catch,
    }
    return render(request, 'third.html', context)
```

## urls.py
```py
from throw_loops import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', views.first),
    path('second/', views.second),
    path('third/', views.third),
]
```