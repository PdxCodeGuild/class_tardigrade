from django.urls import path
from . import views

app_name = 'groceryapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:id>', views.complete, name='complete'),
    path('incomplete/<int:id>', views.incomplete, name='incomplete'),
    path('delete/<int:id>', views.delete, name='delete'),
]