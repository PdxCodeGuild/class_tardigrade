from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home(request):
    context = {'authors': Author.objects.all().order_by('name')}
    return render(request, 'library/home.html', context)

def books(request, id):
    context = {
    'books': get_object_or_404(Book, id=id),
    'authors': get_object_or_404(Author, id=id),
    }
    return render(request, 'library/books.html', context)

def checkout(request, id):
    story = get_object_or_404(Checkout, id=id)
    story.checkout = True
    story.save()
    return redirect('library/checkout.html')

def checkin(request, id):
    ...