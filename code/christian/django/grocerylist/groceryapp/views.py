from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    return HttpResponse('hello world!')

# Create your views here.
