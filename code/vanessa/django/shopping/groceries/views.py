from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Item


def index(request):
    grocery_list = Item.objects.all()
    completed_list = Item.objects.filter(completed=True)
    incomplete_list = Item.objects.filter(completed=False)      
    context = {
        "grocery_list": grocery_list,
        "completed_list": completed_list,
        "incomplete_list": incomplete_list
    }
    return render(request, 'groceries/index.html', context)


def addview(request):
    if request.method =='POST':
        description = request.POST['groceryitem']
        
        Item.objects.create(description=description)
        return redirect('/')

def complete(request, id):
    complete_item= Item.objects.get(id=id)
    complete_item.completed= True
    complete_item.completed_date=timezone.now()
    complete_item.save()
    return redirect ('groceries:index')


def delete_item(request,id):
    del_item= Item.objects.get(id=id)
    del_item.delete()
    return redirect('groceries:index')


# def completed (request):
#     completed_list = Item.objects.filter(completed=True)   
#     context = {
#         "completed_list": completed_list,
#     }
#     return render(request, 'groceries/index.html', context)

# def incomplete (request):
#     incomplete_list = Item.objects.filter(completed=False)   
#     context = {
#         "incomplete_list": incomplete_list,
#     }
#     return render(request,'groceries/index.html', context)
