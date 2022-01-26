from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *

def home(request):
    context = {
    'books': Book.objects.all(),
    'authors': Author.objects.all().order_by('name'),
    }
    return render(request, 'library/home.html', context)

def checkout(request, id):
    checked = get_object_or_404(Book,id=id)
    checked.available = False
    checked.save() 
    context = {
    'books': get_object_or_404(Book, id=id),
    'authors': get_object_or_404(Author, id=id,)
    }
    return render(request, 'library/checkout.html', context)

def user_checkout(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=id)
        name = request.POST['user']
        time = timezone.now()
        checkout = True
        Checkout.objects.create(book=book, user=name, timestamp=time, checkout=checkout)
    context = {
    'books': get_object_or_404(Book, id=id),
    'authors': get_object_or_404(Author, id=id),
    }
    return render(request, 'library/success.html', context)

def checkedout_list(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'checked': Checkout.objects.all(),
    }
    return render (request, 'library/checkedout_list.html', context)

def checkin_list(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'checked': Checkout.objects.all(),
    }
    return render (request, 'library/checkin_list.html', context)

def checkin(request, id):
    checked = get_object_or_404(Book,id=id)
    checked.available = True
    checked.save() 
    context = {
    'books': get_object_or_404(Book, id=id),
    'authors': get_object_or_404(Author, id=id),
    }
    return render(request, 'library/checkin.html', context)

def user_checkin(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=id)
        name = request.POST['user']
        time = timezone.now()
        checkout = False
        Checkout.objects.create(book=book, user=name, timestamp=time, checkout=checkout)
    return render(request, 'library/success.html')
   