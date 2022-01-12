from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render 
from .models import GroceryItem
from django.http import HttpResponse
from django.utils import timezone


def index(request):
    incomplete_list = GroceryItem.objects.filter(completed=False)
    completed_list = GroceryItem.objects.filter(completed=True)
    list = GroceryItem.objects.all()
    context = {'list': list, 
    'completed_list': completed_list,
    'incomplete_list': incomplete_list
    }
    return render(request, 'groceryapp/mytemplate.html', context)

def add_item(request):
    text = request.POST.get('text')
    GroceryItem.objects.create(text=text)
    return redirect('/')

def remove_item(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()
    return redirect('/')

def complete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.completed = True
    item.completed_date = timezone.now()
    item.save()  
    return redirect('/')


    
    
    
# def completed(request):


# def mycreate(request):
#     myfield = request.POST['myfield']
#     mymodel = MyModel(myfield=myfield)
#     mymodel.save()
#     print(request.POST)
#     return HttpResponseRedirect(reverse('groceryapp:myview'))

# Create your views here.


