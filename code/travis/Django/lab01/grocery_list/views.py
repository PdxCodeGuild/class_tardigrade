from django.http import HttpResponse
from django.shortcuts import render
from .models import GroceryItem
from datetime import datetime


# def index(request):
#     context = {GroceryItem.description: ..., GroceryItem.created_date: ..., GroceryItem.completed_date:..., GroceryItem.completed:...}
#     return render(request, 'grocery_list/index.html', context)


def index(request):

    grocery_item_list = GroceryItem.objects.all()
    print(grocery_item_list)


    # for g in grocery_item_list:

    #     output = g.description
    #     output2 = g.created_date.strftime('%m/%d/%y')

    #     for g in grocery_item_list:

    #         if g.completed_date is None:

    #             output3 ="Not completed"        
    #         else:

    #             output3 = g.completed_date.strftime('%m/%d/%y')
        
    #     output4 = str(g.completed)

    context = {'grocery_item_list': grocery_item_list}
    
    return render(request, 'grocery_list/index.html', context)
    #return HttpResponse("item:" + output + " created date:" + output2  + "completed date:" + output3 + output4)



""" 
    output = ','.join([g.description for g in grocery_item_list])
    output2 = ','.join([g.created_date.strftime('%m/%d/%y') for g in grocery_item_list])
  
    for g in grocery_item_list:

        if g.completed_date is None:
            print("none test")
            output3 ="".join("Not completed")         
        else:
            output3 = "".join(g.completed_date.strftime('%m/%d/%y'))


    output4 = ','.join([str(g.completed) for g in grocery_item_list]) """

    