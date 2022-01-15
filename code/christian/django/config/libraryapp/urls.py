from django.urls import path
from . import views

app_name = 'libraryapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkinout/<int:id>/', views.checkinout, name='checkinout'),
    path('checkedout/<int:id>/', views.checkedout, name='checkedout'),
    path('history', views.history, name='history')
    
    
]