from django.urls import path

from . import views


app_name ='grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('complete', views.complete, name='complete'),
    path('delete', views.delete, name='delete'),

]
