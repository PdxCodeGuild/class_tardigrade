from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author

def index(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
    }
    return render(request,'bookshelf/index.html',context)

# def add(request):
#     ...
# def delete(request):
#     ...
# def checkout(request):
#     ...
# def book_lookup(request):
#     ...
# def author_lookup(request):
#     ...
