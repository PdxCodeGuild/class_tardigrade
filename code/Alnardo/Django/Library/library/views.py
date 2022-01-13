from django.http.response import HttpResponse
from django.shortcuts import render


from .models import Book, Author

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
    # return HttpResponse('Not my problem')