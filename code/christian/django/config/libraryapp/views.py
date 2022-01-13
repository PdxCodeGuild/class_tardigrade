from django.shortcuts import render
from django.http import HttpResponse
from .models import author, book 

def index(request):
    myinstances = author.objects.all()
    myinstances = book.objects.all()
    context = {
        'author': author
    }
    return render(request, 'libraryapp/template.html', context)

def book(request):


# Create your views here.
