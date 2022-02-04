from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get-todos/', views.get_todos),
    path('add-new-todo/', views.add_new_todo)
]