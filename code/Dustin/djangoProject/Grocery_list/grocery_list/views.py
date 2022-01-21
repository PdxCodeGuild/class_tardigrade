from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Items

class grocerylist(ListView):
    model = items
# Create your views here.

class ItemCreate(CreateView)
    