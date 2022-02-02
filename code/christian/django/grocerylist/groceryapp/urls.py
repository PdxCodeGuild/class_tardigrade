from django.urls import path
from . import views

app_name = 'groceryapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('newitem/', views.add_item, name='newitem'),
    path('remove_item/<int:id>/', views.remove_item, name='remove_item'),
    path('complete/<int:id>/', views.complete, name='complete')
    # path('mycreate/', views.mycreate, name='mycreate')
]