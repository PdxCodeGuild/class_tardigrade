from django.urls import path
from . import views

app_name = 'chirp' # for namespacing
urlpatterns = [
    path('login/', views.login, name='main'),
   # path("login/", views.login, name= "login"),
]