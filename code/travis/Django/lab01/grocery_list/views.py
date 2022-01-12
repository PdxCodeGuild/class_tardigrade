from django.http import HttpResponse
from django.shortcuts import render
from .models import GroceryItem
from datetime import datetime


def index(request):

    grocery_item_list = GroceryItem.objects.all() 

    context = {'grocery_item_list': grocery_item_list}
    
    return render(request, 'grocery_list/index.html', context)

