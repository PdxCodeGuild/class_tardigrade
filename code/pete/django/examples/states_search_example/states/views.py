from django.shortcuts import render
from django.db.models import Q

from .models import State

def index(request):
    context = {'states': State.objects.all()} # SELECT * FROM state_states;

    if request.method == 'POST':
        term = request.POST.get('term')
        matching_states = State.objects.filter(Q(name__icontains=term) | Q(abbreviation__icontains=term)) # SELECT * FROM state_states WHERE state.name LIKE term OR state.abbreviation LIKE term (probably not right!!)
        context = {'states': matching_states}
    
        
        

    return render(request, 'states/index.html', context)
