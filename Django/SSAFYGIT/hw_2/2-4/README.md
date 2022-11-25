# project4/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("chatting/", include("chatting.urls")),
    # informations를 informtion으로 수정
    path("information/", include("information.urls")),
    path("admin/", admin.site.urls),
]
```

# chatting/views.py
```py
from django.shortcuts import render

# Create your views here.
def index(request):
    # temaplates에 chatting 폴더 추가
    return render(request, 'chatting/index.html')
```

# information/views.py
```py
from django.shortcuts import render

# Create your views here.
def index(request):
        # temaplates에 information 폴더 추가
    return render(request, 'information/index.html')
```