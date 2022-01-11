from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import GroceryItem
from datetime import datetime

from django import forms


def index(request):


    if request.method == 'POST':
        
        print(request.POST)

        description = request.POST["description"]
        created_date = request.POST["created_date"]
        completed_date = None
        completed = False
        
        new_item = GroceryItem(description = description, created_date = created_date, completed_date = completed_date, completed=completed)

        new_item.save()

       # data = dict(request.POST)

    



    grocery_item_list = GroceryItem.objects.all() 

    context = {'grocery_item_list': grocery_item_list}
    
    return render(request, 'grocery_list/index.html', context)




def complete(request):
  #  print(request.POST)
    id_entry = request.POST["id"]

    entry = get_object_or_404(GroceryItem, id = id_entry)


    context = entry[complete: True]

    #new_item = GroceryItem(id = id_entry,  completed=True)

    print(entry)
   # print(new_item)
   # grocery_item_list.save()
    print(context)

    grocery_item_list = GroceryItem.objects.all() 

    context = {'grocery_item_list': grocery_item_list}

    return render(request, 'grocery_list/complete.html', context)


def delete(request,id):
    ...