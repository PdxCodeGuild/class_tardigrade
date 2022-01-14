from django.urls import path
from . import views




app_name = 'library' # for namespacing
urlpatterns = [
    path('', views.library, name='library'),

  path("checked-out/<int:id>/", views.library, name="title"),

  path("<int:id>/book", views.library, name="title")


]