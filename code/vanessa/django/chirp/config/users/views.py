from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def username_exists(username):
    return User.objects.filter(username=username).exists()

def login_view(request):
    message = ''
    if request.method == 'POST':
        print("hello")
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("if statement ran")
            login(request, user)
            return redirect('/')
        else:
            print("else statement ran")
            message = 'please input proper credentials'
    context = {'message': message}
    print("no post")
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    message = ''
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        
        if username_exists(username):
            message += ' username taken'

        if password1 != password1:
            message += ' passwords do not match'
        
        if message:
            context = {'message': message}
            return render(request, 'users/register.html', context)

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('/')
        
    return render(request, 'users/register.html')