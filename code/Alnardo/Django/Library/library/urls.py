from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('checkout/', views.checkout, name='checkout'),
]

