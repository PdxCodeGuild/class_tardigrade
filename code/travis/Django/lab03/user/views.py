from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def login(request):
    return HttpResponse('hello world!')





def mylogin(request):

    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        redirect("")
    else:
        # return an 'invalid login' error message
        redirect("")
    
    return HttpResponse("login page")



def logout_view(request):
    logout(request)
    # redirect to a success page.
    redirect("")
    return HttpResponse("logout")






#from django.contrib.auth.models import User
#user = User.objects.get(username='jane')
#user.set_password('newpassword')
#user.save()

