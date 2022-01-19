from django.urls import path
from . import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<int:id>',views.checkout, name="checkout"),
    path('new_page',views.new_page, name='new_page'),
    path('author_page',views.author_page, name='author_page'),
    path('books_page',views.books_page, name='books_page'),
    path('user/<int:id>',views.user, name='add')
]
    