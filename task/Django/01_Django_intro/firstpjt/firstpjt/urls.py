"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # articles
    path('admin/', admin.site.urls), # url에 admin/를 쓰면 어드민 페이지로 가라라는 뜻
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),


    # path('index/', views.index),
    # path('greeting/', views.greeting), # Django는 마지막에 ','를 붙이도록 권장함
    # path('dinner/', views.dinner),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('hello/<str:name>/', views.hello), # '<>'가 들어가면 변수역할 'str:'안적어도 문자열이 기본값임

    # # pages
    # path('pages-index/', pages_views.index),
]
