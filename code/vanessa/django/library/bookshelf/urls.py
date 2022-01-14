from django.urls import path
from . import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<int:id>',views.checkout, name="checkout"),
]
    