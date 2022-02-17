from django.utils import timezone
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect


from .models import Book, Author, return_date_time, Check_Out

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    available = Check_Out.objects.filter(checked_out=False)
    not_available = Check_Out.objects.filter(checked_out=True)

    context = {
        'books' : books,
        'authors' : authors,
        'available' : available,
        'not_available' : not_available,
    }
    return render(request, 'library/index.html', context)

def detail(request, id):
    book = get_object_or_404(Book, id=id)
    most_recent_checkout = Check_Out.objects.filter(book=book).last()
    context = {'book' : book,
                'most_recent_checkout':most_recent_checkout}

    return render(request, 'library/detail.html', context)

def check_out_book(request, id):
    checkout_book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        user_input = request.POST.get('user')
        Check_Out.objects.create(book=checkout_book,user=user_input)
    return redirect('library:index')


def return_book(request, id):
    returned_book = get_object_or_404(Check_Out, id=id)
    returned_book.checked_out = False
    returned_book.save()
    return redirect('library:index')


def checkout_list(request):
    checked_out_book = Check_Out.objects.filter(checked_out=True).order_by('-id')
    returned_book = Check_Out.objects.filter(checked_out=False).order_by('-id')
    context = {'checked_out_book' : checked_out_book,
                'returned_book': returned_book}
    return render(request, 'library/checkout.html', context)
