from django.shortcuts import render, get_object_or_404

from .models import State, Person

def index(request):
    context = {
        'states': State.objects.all()
    }
    return render(request, 'census/index.html', context)

def state(request, slugified_name):
    # example slugs: 'Oregon' -> 'oregon'
    # 'New Mexico' => 'new-mexico'
    context = {
        'state': get_object_or_404(State, slug=slugified_name)
    }
    return render(request, 'census/state.html', context)

def person(request, id):
    context = {
        # get the person with the id passed in
        # if that person does not exist, raise a 404
        'person': get_object_or_404(Person, id=id)
    }
    return render(request, 'census/person.html', context)