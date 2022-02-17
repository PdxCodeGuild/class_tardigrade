from django.shortcuts import redirect, render 
from .models import author
from .models import book
from .models import checkout

# Create your views here.
from django.http import HttpResponse


def myview(request):
    books = book.objects.all()
    checkouts = checkout.objects.all()
    
    context = {
        'books': books,
        'checkout':checkouts
    }
    
    return render(request, 'libraryapp/mytemplate.html', context)

def mycreate(request):
    if request.method == 'POST':
        data = dict(request.POST)
        book_id=request.POST.get('book')
        book_object=book.objects.get(id=book_id)
        print(book_object)
        checkout.objects.create(book=book_object, user=data['user'])
        print(request.POST)
    return redirect('myapp:myview')





