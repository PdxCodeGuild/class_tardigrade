from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .models import Post

def index(request):
    if request.user.is_authenticated:
        # groceries = GroceryItem.objects.all() # pre-user version
        groceries = request.user.groceries.all()
        print(groceries) # <QuerySet [<GroceryItem: apples>, <GroceryItem: spindrift>, <GroceryItem: flintstones vitamins>]>
        context = {'groceries': groceries}
        print(request.user)
        return render(request, 'chirp/index.html', context)
    return render(request, 'chirp/index.html')


def add(request):
    print(request.POST)
    description_from_form = request.POST.get('description', '')
    GroceryItem.objects.create(
        description=description_from_form,
        user=request.user,
        # these were addressed in the model
        # created_date=timezone.now(),
        # completed=False
    )
    return redirect('/')

@require_http_methods(['POST'])
def delete(request, id):
    grocery = get_object_or_404(GroceryItem, id=id, user=request.user)
    # safer method than
    # grocery = GroceryItem.objects.get(id=id)
    grocery.delete()
    return redirect('/')

@require_http_methods(['POST'])
def complete(request, id):
    grocery = get_object_or_404(GroceryItem, id=id, user=request.user)
    if grocery.completed: # item is completed, mark it uncomplete
        grocery.completed = False
        grocery.completed_date = None
    else: # item isn't completed, mark it complete
        grocery.completed = True
        grocery.completed_date = timezone.now()
    grocery.save()
    return redirect('/')

@require_http_methods(['POST'])
def post(request, id):
    context = {
        'post': get_object_or_404(Post, id=id)
    }
    return render(request, 'blog/post.html', context)