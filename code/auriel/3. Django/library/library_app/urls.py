from django.urls import path
from . import views

app_name = 'library_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.checkout, name='checkoutpage')
]