from django.urls import path
from . import views




app_name = 'library' # for namespacing
urlpatterns = [
  path('', views.library, name='library'),
  
  path("library-checkout/", views.checkout),
  path("library-checkout/checked-out/<int:id>/", views.checkout_book),
]