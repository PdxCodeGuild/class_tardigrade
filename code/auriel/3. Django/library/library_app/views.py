from multiprocessing import context
from turtle import title
from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    context = {'authors': Author.objects.all().order_by('name')}
    return render(request, 'library/home.html', context)

def books(request, id):
    context = {'books': get_object_or_404(Book, id=id)}
    return render(request, 'library/books.html', context)