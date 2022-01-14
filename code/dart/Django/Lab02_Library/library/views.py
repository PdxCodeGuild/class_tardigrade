from django.shortcuts import render, redirect
from .models import Book, Author, Checked
from .form import LibraryForm

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors,
        'checked': Checked.objects.all(),
    }
    return render(request, 'library/index.html', context)

def form(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('library:index')
    form = LibraryForm()
    context = {'form': form}
    return render(request, 'library/checkout.html', context)

def checkin(request, id):
    id = request.POST['id']
    returned = Checked.objects.get(id=id)
    returned.checked_out = False
    returned.save()
    return redirect('library:index')
