from django.db.models.fields import NullBooleanField
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import GroceryItem
# Create your views here.
# now = timezone.now()

# def index(request):
#     return HttpResponse('ok')


def index(request):
    if request.method == 'POST':
        description_input = request.POST.get('description')
        # created_date_input = request.POST.get('created_date')
        # completed_input = request.POST.get('completed')
        # boolean_input = request.POST.get('completed')
        GroceryItem.objects.create(description=description_input)
        return redirect('/')
    
    grocery_list = GroceryItem.objects.all().order_by('-completed')
    completed_list = GroceryItem.objects.filter(completed=True)
    incomplete_list = GroceryItem.objects.filter(completed=False)

    context = {'grocery_list' : grocery_list,
                'incomplete_list': incomplete_list,
                'complete_list' : completed_list}

    return render(request, 'grocery/index.html', context)

def detail(request, id):
    grocery_item = get_object_or_404(GroceryItem, id=id)
    context = {'grocery' : grocery_item}
    # if grocery_item.completed == False:
    #     ...
    return render(request, 'grocery/detail.html', context)


def update(request, id):
    grocery_item = get_object_or_404(GroceryItem, id=id)
    if grocery_item.completed == False:
        grocery_item.completed = True
        grocery_item.completed_date = timezone.now()
    else:
        grocery_item.completed = False
        grocery_item.completed_date = None
    grocery_item.save()
    return redirect('grocery:index')

def delete(request,id):
    GroceryItem.objects.filter(id=id).delete()
    return redirect('grocery:index')
