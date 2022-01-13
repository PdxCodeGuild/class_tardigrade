from django.urls import path
from . import views




app_name = 'library' # for namespacing
urlpatterns = [
    path('', views.library, name='library'),

   # path("<int:id>/", views.library, name="author_name"),

  #  path("<int:id>/book", views.library, name="title")


]