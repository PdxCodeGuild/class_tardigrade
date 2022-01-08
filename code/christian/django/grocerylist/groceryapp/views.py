from django.shortcuts import render
from .models import MyModel
from django.http import HttpResponse

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }

    return render(request, 'groceryapp/mytemplate.html', context)

def mycreate(request):
    print(request.POST)
    return HttpResponse('form recieved')

# Create your views here.


