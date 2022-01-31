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
    book = get_object_or_404(Book, id=id)
    timestamp= timezone.now()
    checked_out=True
    description = request.POST['user']
    checkouts = book.checked_out_books.all() # gives you a QuerySet of the CheckOut objects associated with the book
    if checkouts.exists(): # is the CheckOut QuerySet not empty
        checkout = checkouts.last()
        if checkout.checked_out == True:
            print('hello')
            # the book is checked out, can only be returned
        else:
            print('bye')
            # the book is not checked out, is available
    else:
        Check_out_in.objects.create(books=book,timestamp=timestamp,checked_out=checked_out,user_name=description)
    
    checked_item= get_object_or_404(Book,id=id)
    checked_item.checked_out= True
    checked_item.timestamp=timezone.now()
    checked_item.save()
    return redirect('/')

def user(request,id):
    if request.method == 'POST':
        timestamp= timezone.now()
        description = request.POST['user']
        checked_out=True
        book=get_object_or_404(Book, id=id)
        Check_out_in.objects.create(user_name=description, timestamp=timestamp, checked_out=checked_out, books=book)

        return redirect('/')

def check_in(request, id):
        timestamp= timezone.now()
        checked_out=False
        book=get_object_or_404(Book, id=id)
        Check_out_in.objects.create(timestamp=timestamp, checked_out=checked_out, books=book)

        return redirect('/')


def checkout_page(request):
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

def history(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'checkout_history': Check_out_in.objects.all(),
        # 'checkout_history': Check_out_in.objects.filter(checked_out=True)
    }
    return render(request,'bookshelf/history.html',context )