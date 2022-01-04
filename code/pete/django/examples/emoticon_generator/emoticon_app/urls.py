from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('save/<str:emoticon_str>', views.save),

    path('hello/', views.hello),
]