from django.urls import path
from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('start/', views.start, name='start'),
]