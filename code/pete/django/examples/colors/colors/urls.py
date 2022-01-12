from django.urls import path
from . import views

app_name = 'colors'
urlpatterns = [
    path('start/', views.start, name='start'),
    path('colors/', views.colors, name='colors'),
    path('new-color/', views.new_color, name='new_color'),
    path('like-color/<int:id>/', views.like_color, name='like_color'),
]