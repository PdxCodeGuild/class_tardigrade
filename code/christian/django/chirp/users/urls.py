from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.RegisterUser.as_view(), name = 'signup'),
    path('<str:username>/', views.UserProfile.as_view(), name = 'profile')
]