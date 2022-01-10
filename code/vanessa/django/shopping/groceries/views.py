from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Item


def index(request):
    grocery_list = Item.objects.all()
    context = {
        "grocery_list": grocery_list
    }
    print("!!!!!")
    return render(request, 'groceries/index.html', context)


def addview(request):
    if request.method =='POST':
        description = request.POST['groceryitem']
        
        Item.objects.create(description=description)
        return redirect('/')

def complete(request):
    complete_item= Item.objects.get(id=id)
    complete_item= True
    return redirect ('groceries:index.html', context)



def delete_item(request,id):
    del_item= Item.objects.get(id=id)
    del_item.delete()
    return redirect('groceries:index')
