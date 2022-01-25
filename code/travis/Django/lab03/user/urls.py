from django.urls import path
from . import views

app_name = 'user' # for namespacing
urlpatterns = [

 #   path("../", views)    ###redirect to chirp submit


    path('accounts/login/', views.mylogin, name='login'),
    path("accounts/logout/", views.logout_view, name= "logout"),
]