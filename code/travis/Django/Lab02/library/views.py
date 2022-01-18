from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from library.models import Book
from library.models import CheckoutBook




def library(request):

    book_list = Book.objects.all()
    context = {'book_list': book_list}

    return render(request, 'library/library.html', context )




def checkout(request):


  checkout_list = CheckoutBook.objects.all()


  context = {'checkout_list': checkout_list}

  return render(request, 'library/library_checkout.html', context )






def checkout_book(request, id):
    print(request)
    checkout_book_list = get_object_or_404(CheckoutBook, id = id)
   # user_submit = request.POST[id.user]

    #if checkout_book_list.is_checked_out == True:
    #  checkout_book_list.is_checked_out = False
     # checkout_book_list.user = user_submit
    #  checkout_book_list.time_stamp = 1234

   # else:

   #   checkout_book_list.is_checked_out = True




   #   checkout_book_list.time_stamp = 1234

   # checkout_book_list.save()
    # checkout_list = CheckoutBook.objects.all()


    # context = {'checkout_list': checkout_list}

    return render(request, 'library/library_checkout.html' )