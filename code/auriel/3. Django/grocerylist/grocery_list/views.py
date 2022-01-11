from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import GroceryItem

def home(request):
    groceryitem = GroceryItem.objects.all()
    context = {'groceryitem': groceryitem}
    return render(request, 'grocery_list/groceryitems.html', context)


def add(request):
    item = request.POST.get('item')
    GroceryItem.objects.create(description = item)
    return redirect('/')

def complete(request, id):
    ...

def delete(request, id):
    ...
