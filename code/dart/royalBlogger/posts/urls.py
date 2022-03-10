from unicodedata import name
from . import views
# from .views import UpdatePostView
from django.urls import path

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('detail/<int:pk>', views.post_detail, name='post_detail'),
    # path('edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
]
