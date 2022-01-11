from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import GroceryItem
from django.utils import timezone


def home(request):
    groceryitem = GroceryItem.objects.all()
    context = {'groceryitem': groceryitem}
    return render(request, 'grocery_list/groceryitems.html', context)
