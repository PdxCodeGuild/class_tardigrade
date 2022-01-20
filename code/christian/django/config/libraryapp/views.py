from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Author, Book, Checkout 

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books
    }
    return render(request, 'libraryapp/template.html', context)

def checkinout(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'book': book}
    return render(request,'libraryapp/checkinout.html', context)

def checkedout(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        user = request.POST['user']
        checkout = True
        Checkout.objects.create(user = user, book = book, checkout = checkout)
        return redirect('/history')

def checkedin(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        user = request.POST['user']
        checkout = False
        Checkout.objects.create(user = user, book = book, checkout = checkout)
        return redirect('/history')


def history(request):
    history = Checkout.objects.all()
    context = {'checkouts': history}
    return render(request, 'libraryapp/history.html', context)





