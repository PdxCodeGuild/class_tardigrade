from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def username_exists(username):
    return User.objects.filter(username=username).exists()

def login_view(request):
    message = ''
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = 'Invalid User Credentials'
    context = {'message': message}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    message = ''
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if username_exists(username):
            message += ' Username Is Already In Use'

        if password1 != password2:
            message += ' Passwords Do Not Match'
        
        if message:
            context = {'message': message}
            return render(request, 'users/sign_up.html', context)

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('/')
        
    return render(request, 'users/sign_up.html')