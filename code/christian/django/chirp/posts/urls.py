from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('post/<int:pk>/', views.PostDetail.as_view(), name = 'detail'),
    # path('post/new/', views.PostCreate.as_view(), name='new'),
    # path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='edit'),
    # path('post/<int:pk>/delete/', views.PostDelete.as_view(), name = 'delete')
]