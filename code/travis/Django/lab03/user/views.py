from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserLoginForm



def mylogin(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect("/")

        else:

            return redirect("/")

    login_form = UserLoginForm()

    return render(request, 'user/login.html', {'login_form': login_form})


def logout_view(request):

    logout(request)

    return redirect("/")


def create_user(request):


    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username, None, password)
        user.save()

        return redirect("/")

    create_form = UserLoginForm()
    
    return render(request, 'user/register.html', {'create_form': create_form})
