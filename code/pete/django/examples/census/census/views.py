from django.shortcuts import render, get_object_or_404

from .models import State

def index(request):
    context = {
        'states': State.objects.all()
    }
    return render(request, 'census/index.html', context)

def state(request, slugified_name):
    context = {
        'state': get_object_or_404(State, slug=slugified_name)
    }
    return render(request, 'census/state.html', context)
