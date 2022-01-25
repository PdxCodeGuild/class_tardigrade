from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *

def home(request):
    context = {
    'books': Book.objects.all(),
    'authors': Author.objects.all().order_by('name'),
    }
    return render(request, 'library/home.html', context)

def checkout(request, id,):
    checked = get_object_or_404(Book,id=id)
    checked.available = False
    checked.save() 
    context = {
    'books': get_object_or_404(Book, id=id),
    'authors': get_object_or_404(Author, id=id,),
    }
    return render(request, 'library/checkout.html', context)