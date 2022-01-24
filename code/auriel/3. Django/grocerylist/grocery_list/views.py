from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import GroceryItem
from django.utils import timezone
from django.urls import reverse


def home(request):
    groceryitem = GroceryItem.objects.all()
    context = {'groceryitem': groceryitem}

    return render(request, 'grocery_list/groceryitems.html', context)

def add(request):
    item = request.POST.get('item')
    GroceryItem.objects.create(description = item)
    return redirect('/')

def complete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.completed = True
    item.completed_date = timezone.now()
    item.save()
    return redirect('/')

def delete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()    
    return redirect('/')
