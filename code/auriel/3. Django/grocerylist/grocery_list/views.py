from django.shortcuts import render
from django.http import HttpResponse


def start(request):
    return HttpResponse('Welcome to your Grocery List')