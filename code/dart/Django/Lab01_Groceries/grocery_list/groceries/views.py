from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import GroceryItem

def index(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        GroceryItem.objects.create(item=item, created_date=timezone.now())
        return redirect('groceries:index')
    
    groceries = GroceryItem.objects.all()
    completed_groceries = GroceryItem.objects.filter(completed=True)
    incomplete_groceries = GroceryItem.objects.filter(completed=False)

    context = {'groceries': groceries, 'completed_groceries': completed_groceries, 'incomplete_groceries': incomplete_groceries}
    return render(request, 'groceries/index.html', context)

def delete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()
    return redirect('groceries:index')

def complete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.completed = True
    item.completed_date = timezone.now()
    item.save()
    return redirect('groceries:index')