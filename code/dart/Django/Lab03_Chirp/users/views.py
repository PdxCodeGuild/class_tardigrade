from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def username_exists(username):
    return User.objects.filter(username=username).exists()

def login_user(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:index')

        else:
            message = 'invalid user credentials'
    context = {'message': message}
    return render(request, 'users/login.html', context)

def register_user(request):
    message = ''
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if username_exists(username):
            message += ' username taken'

        if password1 != password2:
            message += ' passwords do not match'
        
        if message:
            context = {'message': message}
            return render(request, 'users/register.html', context)

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('/')
        
    return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    return redirect('posts:index')
