from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .models import chirp
from webbrowser import get

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

def add(request):
    print(request.POST)
    description_form = request.POST.get('description', '')
    chirp.objects.create (
        description=description_form,
        user=request.user,
    )
    return redirect ('/')

@require_http_methods(['POST'])
def delete(request, id):
    chirp = get_object_or_404 (chirp, id=id, user=request)
    chirp.delete()
    return redirect('/')
@require_http_methods(['POST'])
def complete(request,id):
    chirp=get_object_or_404(chirp,id=id, user=request.user)
    if chirp.completed:
        chirp.completed = False
        chirp.completed = None
    else:
        chirp.completed = True
        chirp.completed_date = timezone.now( )
        chirp.save()
        return redirect('/')