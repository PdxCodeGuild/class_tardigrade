import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.models import User

#from code.travis.Django.lab03 import user
from .forms import ChirpForm
from .models import Chirp


from django.contrib.auth import *
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect




def main(request):

    #sorts into newest first
    chirp_list = Chirp.objects.all().order_by("-post_date")
    context = {'chirp_list': chirp_list}

    return render(request, 'chirp/index.html', context)



@login_required
def submit(request):

    if request.user.is_authenticated:
        print("test logged in")

        if request.method == 'POST': # receiving a form submission
         # create an instance of our form from the form data
            form = ChirpForm(request.POST)
            print("inside post check")

            print(form)
            if form.is_valid():
                print("form is valid")
                # get the data out of the form
                username = request.user.username
                post_date = datetime.datetime.now()  
                title = form.cleaned_data["title"]
                message = form.cleaned_data["message"]
#                test = Chirp.objects.get(username = request.user.username)
                
                test = Chirp.objects.filter(username = username)   
                print(test)
                  #  grocery_item_list_test.update(completed_date = datetime.now(), completed = True)


               # print(f"user {username}")
                # create an instance of our model from the data
               # new_chirp = Chirp( User.username = username, title=title, message = message, post_date = post_date)
                # save a new record to the database
              #  print(new_chirp)
              #  new_chirp.save()
                # create a new blank form for the template
                return redirect("/")
        else: # receiving a GET request

            form = ChirpForm() # create a new blank form
            
    else:

        print("test notlogged in")
        
        return redirect("./account/login")
   


    return render(request, 'chirp/submit.html', {'form': form}) # pass the form to the template

