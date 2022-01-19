from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Book, Author, Check_out_in

def index(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),

    }
    return render(request,'bookshelf/index.html',context)


def checkout(request,id):
    checked_item= get_object_or_404(Book,id=id)
    checked_item.checked_out= True
    checked_item.checkout_time=timezone.now()
    checked_item.save()
    return redirect('/')

def user(request):
    if request.method == 'POST':
        description = request.POST['user']
        user.objects.create(description=description)
        return redirect('/')

def new_page(request):

    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'checked_out': Check_out_in.objects.all(),
    }
    return render(request, 'bookshelf/checked_out.html', context)

def author_page(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
      
    }
    return render(request, 'bookshelf/author.html', context )

def books_page(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),

    }
    return render(request, 'bookshelf/books.html', context )