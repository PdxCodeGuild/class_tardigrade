from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Author, Book 

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books
    }
    return render(request, 'libraryapp/template.html', context)

def checkinout(request, id):
    book = get_object_or_404(Book, id=id)
    book.checkout = True
    book.save()
    context = {'book': book}
    return render(request,'libraryapp/checkinout.html', context)

# def form(request):
#     if request.method == 'POST':
#         checkin = request.POST['checkin']
#         checkout = request.POST['checkout']

        
        # title = request.POST['title']
        # body = request.POST['body']
        # Entry.objects.create(title=title, body=body)
        # return redirect('/')
        # return redirect('diary:index')


# def checkin(request, id):
#     book = get_object_or_404(Book, id=id)
#     book.checkout = False
#     book.save()
#     context = {'book': book}
#     return render(request,'libraryapp/checkedin.html', context)



# Create your views here.
#make a form for checkinout
#make html for history of checkin/checkout (myinstance = Model.objects.all())