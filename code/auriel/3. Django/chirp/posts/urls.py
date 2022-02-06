from django.urls import path
from . import views

app_name = 'posts' 
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('user/<int:id>',views.profile, name='profile'),
]