from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import choice

from .models import Emoticon

def index(request):
    eyes = [':', ';']
    nose = ['>', '^']
    mouth = [')', '(', ']']
    emoticon = choice(eyes) + choice(nose) + choice(mouth)

    saved_emoticons = Emoticon.objects.all() # Model.objects.all() returns a QuerySet of all with every Model from the database
    print(saved_emoticons)
    # the context dictionary is how you pass variables into a template
    context = {
        'emoticon': emoticon,
        'saved_emoticons': saved_emoticons,
    }
    # print(emoticon)
    return render(request, 'emoticon_app/index.html', context)

def save(request, emoticon_str):
    Emoticon.objects.create(emoticon=emoticon_str)
    # the redirect function can redirect to another view
    return redirect('/')

def hello(request):
    messages = ['hello world', 'django is fun', 'django is not so fun']
    # HttpResponse returns an instance of a reponse as a string
    return HttpResponse(choice(messages))
