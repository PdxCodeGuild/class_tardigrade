from django.urls import path
from .import views

app_name = 'chirp'
urlpatterns = [
    path('',views.firsttest, name='firsttest')
]