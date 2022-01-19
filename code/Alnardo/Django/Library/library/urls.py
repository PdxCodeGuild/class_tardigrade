from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('check-out/<int:id>/', views.check_out_book, name='check_out'),
    path('return/<int:id>', views.return_book, name='return'),
    path('checkout-list/', views.checkout_list, name='checkout_list'),
]

