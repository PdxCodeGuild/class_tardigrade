from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Book, Author

def index(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        # 'checkout time': Book.checkout_time
    }
    return render(request,'bookshelf/index.html',context)


def checkout(request,id):
    checked_item= get_object_or_404(Book,id=id)
    checked_item.checked_out= True
    checked_item.checkout_time=timezone.now()
    checked_item.save()
    return redirect('/')
