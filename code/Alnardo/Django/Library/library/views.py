from django.http.response import HttpResponse
from django.shortcuts import render


from .models import Book, Author

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books' : books,
        'authors' : authors
    }
    return render(request, 'library/index.html', context)
    # return HttpResponse('Not my problem')