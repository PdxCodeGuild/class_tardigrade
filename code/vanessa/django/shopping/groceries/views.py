from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


def index(request):
    grocery_list = Item.objects.all()
    context = {
        "grocery_list" : grocery_list
    }
    return render(request, 'groceries/index.html', context)
