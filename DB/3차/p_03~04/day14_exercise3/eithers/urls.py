from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/comment', views.comment, name='comment'),
    path('<int:pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    path('random_page/', views.random_page, name='random_page'),
]
