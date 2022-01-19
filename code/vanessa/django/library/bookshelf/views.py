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

def user(request,id):
    if request.method == 'POST':
        timestamp= timezone.now()
        checked_out=True
        book=get_object_or_404(Book, id=id)
        description = request.POST['user']
        Check_out_in.objects.create(user_name=description, timestamp=timestamp, checked_out=checked_out, books=book)

        return redirect('/')

# class Check_out_in(models.Model):
#     checked_out=models.BooleanField(default=False)
#     books=models.ForeignKey(Book, on_delete=models.PROTECT,related_name='checked_out_books', null=True, blank =True)
#     timestamp=models.DateField(null=True, blank =True)
#     user_name=models.CharField(max_length=25)

def new_page(request):

    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'checked_out': Check_out_in.objects.all(),
    }
    return render(request, 'bookshelf/checked_out.html', context)

def check_in(request, id):
    # create an instance of checkout model
    # get the book object for the book
    #update the books checkout status
    return render(request, 'bookshelf/checked_out.html',)


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