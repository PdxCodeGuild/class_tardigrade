from django.urls import path
from . import views

app_name = 'diary' # app_name is for url reverse lookup
urlpatterns = [
    path('', views.index, name='index'), # name= kwarg is for url reverse lookup
    path('entry/<int:id>/', views.detail, name='entry'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]