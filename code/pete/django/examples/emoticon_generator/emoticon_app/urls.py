from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # <str:emoticon_str> will pass a variable that passes as a string into the views.save
    path('save/<str:emoticon_str>', views.save),

    path('hello/', views.hello),
]