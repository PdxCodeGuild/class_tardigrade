from django.urls import path
from . import views




app_name = 'library' # for namespacing
urlpatterns = [
  path('', views.library, name='library'),  
  path("library-checkout/", views.checkout),
  path("library-checkout/<int:id>/", views.checkout_book, name="checkout"),
  path("library-checkin/<int:id>/", views.checkout_book, name="checkin"),
]