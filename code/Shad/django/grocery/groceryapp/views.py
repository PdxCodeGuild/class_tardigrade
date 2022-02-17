from .models import Grocery

from django.shortcuts import redirect, render
from django.http import HttpResponse


def myview(request):
    return HttpResponse('hello world!')


# Create your views here.


def index(request):
    if request.method == 'POST':

        description = request.POST['description']
        GroceryItem.objects.create(description=description)
        return redirect('/')


    grocery_list = GroceryItem.objects.all()  # get all the GroceryItems
    completed_list = GroceryItem.objects.filter(
        completed=True)  # get the completed GroceryItems
    incomplete_list = GroceryItem.objects.filter(
        completed=False)  # get the completed GroceryItems

    context = {
        'grocery_list' : grocery_list

    } 
    return render(request, 'groceryapp/mytemplate.html', context)


"""
Note: there are multiple ways to complete/delete GroceryItems
The following is just a suggestion
"""


def complete(request, id):
    # use the id to get the object from the database
    # change it's completed attribute to True
    # save it
    # redirect back to the home page
    ...


def delete(request, id):
    # use the id to get the object from the database
    # delete it
    # redirect back to the home page
    ...


def myview(request):
    myinstances = GroceryItem.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'groceryapp/mytemplate.html', context)


def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')
