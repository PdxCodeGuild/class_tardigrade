from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from library.models import Book




def library(request):


  #  book = get_object_or_404(Book, pk=id)
    book_list = Book.objects.all()
    context = {'book_list': book_list}



    return render(request, 'library/library.html', context )