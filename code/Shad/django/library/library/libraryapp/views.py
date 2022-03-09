from django.shortcuts import render
from .models import author
from .models import book
# Create your views here.
from django.http import HttpResponse

def myview(request):
    books = book.objects.all()
    context = {
        'books': books
    }
    
    return render(request, 'libraryapp/mytemplate.html', context)

def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')