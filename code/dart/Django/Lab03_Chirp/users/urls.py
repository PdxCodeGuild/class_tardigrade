from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('sign_up/', views.sign_up),
]