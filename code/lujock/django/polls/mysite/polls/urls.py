from django.http.response import HttpResponse
from django.urls import render

def index(request):
    return HttpResponse('hi')