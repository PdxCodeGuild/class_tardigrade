from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    # path('checkout/<int:id>/', views.checkout, name='checkout'),
    # path('checkin/<int:id>/', views.checkin, name='checkin'),
    path('form/', views.form, name='form'),
    path('returning/<int:id>', views.returning, name='returning'),
]