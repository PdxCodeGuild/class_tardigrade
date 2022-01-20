from django.shortcuts import render

from django.http import HttpResponse
from .forms import PostForm
from .models import Chirp



def main(request):


    return HttpResponse('ok')

def login(request):

    
    return HttpResponse('login ok')




from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST': # receiving a form submission
        # create an instance of our form from the form data
        form = PostForm(request.POST)
        if form.is_valid():
            # get the data out of the form
            contact_name = form.cleaned_data['contact_name']
            contact_age = form.cleaned_data['contact_age']
            # create an instance of our model from the data
            contact = Chirp(name=contact_name, age=contact_age)
            # save a new record to the database
            contact.save()
            # create a new blank form for the template
            form = PostForm()
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = PostForm() # create a new blank form
    return render(request, 'contacts/index.html', {'form': form}) # pass the form to the template