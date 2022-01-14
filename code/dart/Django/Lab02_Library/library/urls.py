from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('checkin/<int:id>', views.checkin, name='checkin'),
]