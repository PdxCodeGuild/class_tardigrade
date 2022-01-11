from django.urls import path
from . import views

# 'groceries:add'.split(':')  ['groceries', 'add'] localhost:8000/add/
# {% url 'groceries:delete' grocery_item.pk %} ['groceries', 'delete'] localhost:8000/delete/3


app_name = 'groceries' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addview, name='add'),
    path('complete/<int:id>',views.complete, name="complete"),
    path('delete/<int:id>',views.delete_item, name='delete')
    ]

