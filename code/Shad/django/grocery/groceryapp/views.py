
from django.shortcuts import redirect, render
from django.http import HttpResponse


from django.shortcuts import render
from django.utils import timezone

from .models import GroceryItem

def index(request):
	if request.method == 'POST':
		# If there's a POST request, that means the user
		# has submitted a new GroceryItem for the database
		# How do you parse it?
		print(request.POST) # this will show the post request's
		# QueryDict, a dictionary-like object with the contents
		# of the form data
		data = dict(request.POST) # Optionally, turn the QueryDict
		print(data) # into a plain Python dictionary

		# Save the new GroceryItem to the databse!

		# What else?  Return, redirect?  It's up to you!

	# Here you'll put the code that you want to run for a GET request
	# How do you want to get the necessary items from the database?
	# Here are 3 different queries that return different QuerySets
	# You can use one of these or a combination to put into your context
	# dictionary and render the template

	# grocery_list = GroceryItem.objects.all() # get all the GroceryItems
	# completed_list = GroceryItem.objects.filter(completed=True) # get the completed GroceryItems
	# incomplete_list = GroceryItem.objects.filter(completed=False) # get the completed GroceryItems

	# context = {???} # the context dictionary will have all the objects
	# # you want to render in your template
	# # the return line will render the template
	# return render(request, 'grocery_list/index.html', context)

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
        'grocery_list' : grocery_list,
		'completed_list': completed_list,
		'incomplete_list': incomplete_list,
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
	print(id)
	grocery_item = GroceryItem.objects.get(pk=int(id))
	grocery_item.completed = True
	grocery_item.completed_date = timezone.now().date()
	grocery_item.save()
	return redirect('/')





def incomplete(request, id):
    # use the id to get the object from the database
    # change it's completed attribute to True
    # save it
    # redirect back to the home page
	print(id)
	grocery_item = GroceryItem.objects.get(pk=int(id))
	grocery_item.completed = False
	grocery_item.save()
	return redirect('/')


def delete(request, id):
    # use the id to get the object from the database
    # delete it
    # redirect back to the home page
	grocery_item = GroceryItem.objects.get(pk=int(id))
	grocery_item.delete()
	return redirect('/')

def myview(request):
    myinstances = GroceryItem.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'groceryapp/mytemplate.html', context)


def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')
