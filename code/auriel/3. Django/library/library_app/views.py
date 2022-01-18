import re
from django.shortcuts import render, redirect
from .models import *


def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors,
    }
    return render(request, 'library/home.html', context)
