from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book, Author

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = BookForm()
    context = {
        'form': form,
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
    }
    return render(request, 'book_donator/index.html', context)