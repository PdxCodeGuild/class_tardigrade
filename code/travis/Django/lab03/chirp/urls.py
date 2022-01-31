from django.urls import path
from . import views

app_name = 'chirp' # for namespacing
urlpatterns = [
    
    path('', views.main, name='main'),
    path("submit/", views.submit, name= "submit"),
]