from django.urls import path
from . import views

app_name = 'groceryapp'
urlpatterns = [
    path('myview/', views.myview, name='myview')
]