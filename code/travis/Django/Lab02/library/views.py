import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from library.forms import CheckoutForm

from django.contrib import messages
from library.models import Book
from library.models import CheckoutBook


def library(request):

  book_list = Book.objects.all()
  context = {'book_list': book_list}
    
  return render(request, 'library/library.html', context)



def checkout(request):

  checkout_list = CheckoutBook.objects.all()



  checkout_form = CheckoutForm()


  

  return render(request=request, template_name="library/library_checkout.html", context={'checkout_form': checkout_form, 'checkout_list':checkout_list})






def checkout_book(request, id):
  
  print(id)
  print(request)
  instance = get_object_or_404(CheckoutBook, id=id)

  if request.method == "POST":
      
   # checkout_form = CheckoutForm(request.POST, request.FILES)
    checkout_form = CheckoutForm(request.POST, instance=instance)
    print(checkout_form)
    if checkout_form.is_valid():

      user_input = checkout_form.cleaned_data['user'] 
      print(user_input)   
      checkout_form.user_input.update()
     # checkout_form.save()


      messages.success(request, ('Your book was successfully checked out!'))
      return redirect("/library-checkout/")

    else:

      messages.error(request, 'Error saving form')		

      return redirect("library-checkout/")

  checkout_form = CheckoutForm()


  checkout_list = CheckoutBook.objects.all()
  

  

  return render(request=request, template_name="library/library_checkout.html", context={'checkout_form': checkout_form, 'checkout_list':checkout_list})






# def checkout_book(request):

#   print(request)
  

#   if request.method == "POST":
#       id_entry = request.POST["user"]
#       print(id_entry)
  #     id_entry = request.POST["id": id]
  #     print(id_entry)
  #   id_entry = request.POST["checkid"]
  #   print(id_entry)
  #   id_entry = request.POST["id"]
  #   checkout_book_list = CheckoutBook.objects.filter(id=id_entry)
    
  # #  user_entry = checkout_book_list["user"]
    



  #   user_submit = request.user

  #   if checkout_book_list.is_checked_out == True:
  #     checkout_book_list.is_checked_out = False
  #    # checkout_book_list.user = user_entry
  #     checkout_book_list.time_stamp = 1111
  #     checkout_book_list.save()

  #   else:

  #    checkout_book_list.is_checked_out = True
  #   # checkout_book_list.user = user_entry
  #    checkout_book_list.time_stamp = 2222
  #    checkout_book_list.save()
  
   
 

  # checkout_book_list = CheckoutBook.objects.all()

  # context = {'checkout_list': checkout_book_list}

  # return render(request, 'library/library_checkout.html', context)



