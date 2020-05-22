# urlパスを作成
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.table, name='index'),
    path('delete/', views.delete, name='delete'),
    path('register_class/', views.register_class, name='register_class'),
    path('create_class/', views.create_class, name='create_class'),
    path('change_class/', views.change_class, name='change_class'),
    path('save_change_class/', views.save_change_class, name='save_change_class'),
    path('information/', views.information_of_class, name='information'),
    path('upload/', views.upload, name='upload'),
    path('trace/', views.trace, name='trace'),
    path('news/', views.news, name='news'),
]
