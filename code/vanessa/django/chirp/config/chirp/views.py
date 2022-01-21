from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import chirp

def index(request):
    if request.method == 'POST':
        body = request.POST['body']
        chirp.objects.create(body=body)
        return redirect('chirp:index')



    chirps = chirp.objects.all().order_by('-id')
    context = {'chirp': chirps}
    return render(request, 'chirp/index.html', context)

def detail(request, id):
    chirps = get_object_or_404(chirp, id=id)
    context = {'chirp': chirps}
    return render(request, 'chirp/entry.html', context)
