- project1/setting.py
```py
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
```

- project1/urls.py
```py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('memos/',include('memos.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- memos/views.py
```py
@require_http_methods(["GET","POST"])
def create(request):
    if request.method == "POST":
        form = MemoForm(request.POST, request.FILES)
        if form.is_valid():
            memo = form.save()
            return redirect("memos:detail", memo.pk)
    else:
        form = MemoForm()
    context = {
        'form' : form,
    }
    return render(request,'memos/create.html',context)

@require_http_methods(["GET","POST"])
def update(request,pk):
    memo = get_object_or_404(Memo,pk=pk)
    if request.method == "POST":
        form = MemoForm(request.POST, request.FILES, instance = memo)
        if form.is_valid:
            form.save()
            return redirect("memos:detail",memo.pk)
    else:
        form = MemoForm(instance=memo)
    context = {
        'memo':memo,
        'form':form,
    }
    return render(request,"memos/update.html",context)
```

- htmls
```html
<!-- index.html -->
  <img src="{% static 'image/memo.png' %}" alt="memo">

<!-- create.html/update.html -->
  <form action="{% url 'memos:create' %}" method="POST" enctype="multipart/form-data">

<!-- detail.html -->
<img src="{{ memo.image.url }}" alt="{{ memo.image.url }}">
```