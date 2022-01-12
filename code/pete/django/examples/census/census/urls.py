from django.urls import path

from . import views

app_name = 'census'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slugified_name>/', views.state, name='state'),
    path('person/<int:id>/', views.person, name='person'),
]