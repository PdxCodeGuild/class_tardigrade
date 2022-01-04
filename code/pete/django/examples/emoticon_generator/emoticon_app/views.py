from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import choice

from .models import Emoticon

def index(request):
    eyes = [':', ';']
    nose = ['>', '^']
    mouth = [')', '(', ']']
    emoticon = choice(eyes) + choice(nose) + choice(mouth)

    saved_emoticons = Emoticon.objects.all()
    print(saved_emoticons)
    context = {
        'emoticon': emoticon,
        'saved_emoticons': saved_emoticons,
    }
    # print(emoticon)
    return render(request, 'emoticon_app/index.html', context)

def save(request, emoticon_str):
    Emoticon.objects.create(emoticon=emoticon_str)
    return redirect('/')

def hello(request):
    messages = ['hello world', 'django is fun', 'django is not so fun']
    return HttpResponse(choice(messages))
