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

    if request.method == 'POST':

        id_entry = request.POST["id"]
        grocery_item_list_test = GroceryItem.objects.filter(id=id_entry)   

        grocery_item_list_test.update(completed_date = datetime.now(), completed = True)
        

    grocery_item_list = GroceryItem.objects.all() 

    context = {'grocery_item_list': grocery_item_list}

    return render(request, 'grocery_list/complete.html', context)




def delete(request):

    if request.method == 'POST':
        
        id_entry = request.POST["id"]
        grocery_item_list_test = GroceryItem.objects.filter(id=id_entry)

        grocery_item_list_test.delete()
        

    grocery_item_list = GroceryItem.objects.all() 

    context = {'grocery_item_list': grocery_item_list}

    return render(request, 'grocery_list/delete.html', context)