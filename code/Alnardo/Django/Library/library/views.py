from asyncio.windows_events import NULL
from django.utils import timezone
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect


from .models import Book, Author, return_date_time, Check_Out

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    
    available = Book.objects.filter(checked_out=False)
    not_available = Book.objects.filter(checked_out=True)
    
    context = {
        'books' : books,
        'authors' : authors,
        'available' : available,
        'not_available' : not_available
    }
    return render(request, 'library/index.html', context)

def detail(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'book' : book}

    return render(request, 'library/detail.html', context)

def update(request, id):
    book = get_object_or_404(Book, id=id)
    if book.checked_out == False:
        book.return_date = return_date_time()
        book.checked_out = True
    else:
        book.checked_out = False
        book.return_date = timezone.now()
    book.save()
    if request.method == 'POST':
        user_input = request.POST.get('user')
        Check_Out.objects.create(book=book,user=user_input)
    return redirect('library:index')

def checkout(request):
    checked_out = Check_Out.objects.filter(checked_out=True).order_by('-id')
    returned_book = Check_Out.objects.filter(checked_out=False).order_by('-id')
    context = {'checked_out' : checked_out,
                'returned_book': returned_book}
    return render(request, 'library/checkout.html', context)
