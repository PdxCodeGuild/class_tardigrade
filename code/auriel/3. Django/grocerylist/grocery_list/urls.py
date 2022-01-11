from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.home, name='list'),
    path('add/', views.add, name = 'add'),
]