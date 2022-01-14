from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from library.models import Book




def library(request):


  #  book = get_object_or_404(Book, pk=id)
    book_list = Book.objects.all()
    context = {'book_list': book_list}



    return render(request, 'library/library.html', context )



def checkout(request): # a view for receiving a form submission
  
    print(request.POST) # verify we received the form data
    book_title = request.POST['title'] # get the value the user entered into the 'first name' field


