
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404

from library.forms import CheckoutForm

from django.contrib import messages
from library.models import Book
from library.models import CheckoutBook



def library(request):

    book_list = Book.objects.all()
    context = {'book_list': book_list}

    return render(request, 'library/library.html', context)


def checkout(request):

    if request.method == "GET":

        checkout_list = CheckoutBook.objects.all()
        checkout_form = CheckoutForm()

        return render(request=request, template_name="library/library_checkout.html", context={'checkout_form': checkout_form, 'checkout_list': checkout_list})


def checkout_book(request, id):

    instance = get_object_or_404(CheckoutBook, id=id)

    if request.method == "POST":

        checkout_form = CheckoutForm(request.POST, instance=instance)

        if checkout_form.is_valid():

            checkout_form.save()

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

        print(id)
        CheckoutBook.objects.filter(id=id).update(is_checked_out=False)
        CheckoutBook.objects.filter(id=id).update(time_stamp=datetime.now())

    return redirect("/library-checkout/")
