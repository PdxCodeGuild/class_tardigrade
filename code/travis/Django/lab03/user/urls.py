from django.urls import path
from . import views

app_name = 'user' # for namespacing
urlpatterns = [

 #   path("../", views)    ###redirect to chirp submit


    path('login/', views.mylogin, name='login'),
   #path("login/", views.logout_view, name= "fail"),
]