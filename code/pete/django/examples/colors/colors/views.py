from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Color

def start(request):
    return HttpResponse('hello world!')

def colors(request):
    colors = Color.objects.all()
    context = {'colors': colors}
    return render(request, 'colors/colors.html', context)

def new_color(request):
    color = request.POST.get('color')
    Color.objects.create(color=color)
    return redirect('/colors/colors')

def like_color(request, id):
    color = Color.objects.get(id=id)
    color.likes += 1
    color.save()
    return redirect('/colors/colors')
