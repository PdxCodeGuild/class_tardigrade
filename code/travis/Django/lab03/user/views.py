from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserLoginForm
from django.contrib import messages



def mylogin(request):

    
    print(request)
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print("test1")

        print(user)
        if user is not None:
            login(request, user)
            print("test2")

            return HttpResponse("login")

        else:
            print("test3")
            return redirect("./")
    
    login_form = UserLoginForm() # create a new blank form


    return render(request, 'user/login.html', {'login_form': login_form}) # pass the form to the template



def logout_view(request):

    logout(request)

    return HttpResponse("logout")






#from django.contrib.auth.models import User
#user = User.objects.get(username='jane')
#user.set_password('newpassword')
#user.save()

