from django.shortcuts import render
from django.http import HttpResponse
from .forms import ChirpForm
from .models import Chirp


from django.contrib.auth import *
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect




def main(request):

    chirp_list = Chirp.objects.all()
    context = {'chirp_list': chirp_list}

    return render(request, 'chirp/index.html', context)










def login(request):

    
    return HttpResponse('login ok')





def submit(request):
    if request.method == 'POST': # receiving a form submission
        # create an instance of our form from the form data
        form = ChirpForm(request.POST)
        if form.is_valid():
            # get the data out of the form
            contact_name = form.cleaned_data['contact_name']
            contact_age = form.cleaned_data['contact_age']
            # create an instance of our model from the data
            contact = Chirp(name=contact_name, age=contact_age)
            # save a new record to the database
            contact.save()
            # create a new blank form for the template
            form = ChirpForm()
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = ChirpForm() # create a new blank form
    
    return HttpResponse("submit page")
   # return render(request, 'chirp/index.html', {'form': form}) # pass the form to the template





#check if user is logged in format


#@login_required
#def my_view(request):
#            ...







    #user verification format

#def otherview(request):
 #   if request.user.is_authenticated:
  #      ...
        # do something for authenticated users.
   # else:
    #    ...
        # do something else for anonymous users.




#other user tests



#def email_check(user):
 #   return user.email.endswith('@example.com')

#@user_passes_test(email_check)
#def my_view(request):
   # ...






#create user
#user = User.objects.create_user('jane', 'jane@gmail.com', 'janespassword')