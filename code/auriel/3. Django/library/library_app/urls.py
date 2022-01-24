from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.books, name='book'),
    path('checkout/<int:id>/', views.checkout, name='checkoutpage'),
    path('checkedout//<int:id>/', views.user_checkout, name='checkout'),
    path('checkedout/list/', views.checkedout_list, name='checkedout_list'),
    path('checkin/list/', views.checkin_list, name='checkin_list'),
    path('checkin/<int:id>/', views.checkin, name='checkinpage'),
    path('checkedin/<int:id>/', views.user_checkin, name='checkin'),
]