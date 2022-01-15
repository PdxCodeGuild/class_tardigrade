from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from library.models import Book




def library(request):


  #  book = get_object_or_404(Book, pk=id)
    book_list = Book.objects.all()
    context = {'book_list': book_list}

    return render(request, 'library/library.html', context )






def checkout(request, id):


  book_list = get_object_or_404(Book, id = id)

  if book_list.is_checked_out == True:
    book_list.is_checked_out = False

  else:

    book_list.is_checked_out = True

  book_list.save()

  return redirect('/')