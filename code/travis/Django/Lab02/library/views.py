
from asyncio.windows_events import NULL
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404


from library.forms import CheckoutForm

from django.contrib import messages
from library.models import Book, CheckoutBook




def library(request):

    book_list = Book.objects.all()
    context = {'book_list': book_list}

    return render(request, 'library/library.html', context)


def checkout(request):   


    if request.method == "GET":

        bempty = CheckoutBook.objects.all()
        if bempty.exists():
            ...
        else:
            book_list = Book.objects.all()

            for book in book_list:
                test1 = Book.objects.filter(title = book.title)         
                add_book = CheckoutBook( title = Book.objects.get(title = book.title) )
                b = CheckoutBook.objects.all()
              
                if not b:           
                    add_book.save()                
                else:
                    for checkbook in b:  
                       
                        test1 = Book.objects.filter(title = book.title)              
                       
                        if test1.contains(checkbook.title):
                            print("test1")
                            
                        else:    
                            add_book.save()                            
                                    

        checkout_list = CheckoutBook.objects.all()
      
        
        checkout_form = CheckoutForm()

        return render(request=request, template_name="library/library_checkout.html", context={'checkout_form': checkout_form, 'checkout_list': checkout_list})


def checkout_book(request, id):

    instance = get_object_or_404(Book, id=id)

    if request.method == "POST":

        checkout_form = CheckoutForm(request.POST, instance=instance)

        if checkout_form.is_valid():
 
            userform = checkout_form.cleaned_data.get("user")
   
            CheckoutBook.objects.filter(id=id).update(user = userform)
            CheckoutBook.objects.filter(id=id).update(is_checked_out=True)
            CheckoutBook.objects.filter(id=id).update(time_stamp=datetime.now())

            messages.success(
                request, ('Your book was successfully checked out!'))

            return redirect("/library-checkout/")

        else:

            messages.error(request, 'Error saving form')

            return redirect("library-checkout/")


def checkin(request, id):

    if request.method == "POST":
        CheckoutBook.objects.filter(id=id).update(user=None)
        CheckoutBook.objects.filter(id=id).update(is_checked_out=False)
        CheckoutBook.objects.filter(id=id).update(time_stamp=datetime.now())

    return redirect("/library-checkout/")
