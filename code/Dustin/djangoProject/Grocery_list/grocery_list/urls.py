from django.urls import path
from . import views import grocerylist


urlpatterns = [
    path('', grocerylist.as_view, name='items')
]