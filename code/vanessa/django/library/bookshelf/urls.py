from django.urls import path
from . import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<int:id>',views.checkout, name="checkout"),
    path('check_in/<int:id>',views.check_in, name='check_in'),
    path('checkout_page',views.checkout_page, name='checkout_page'),
    path('author_page',views.author_page, name='author_page'),
    path('books_page',views.books_page, name='books_page'),
    path('history',views.history, name='history'),
    path('user/<int:id>',views.user, name='add')
    
]
    