from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import GroceryItem


def index(request):
    return render(request, 'grocery_list/groceryitems.html')