from django.urls import path
from . import views


app_name = 'library'
urlpatterns = [
  path('', views.library, name='library'),  
  path("library-checkout/", views.checkout),
  path("library-checkout/chechout/<int:id>/", views.checkout_book, name="checkout"),
  path("library-checkout/checkin/<int:id>/", views.checkin, name="checkin"),
] 

