from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# import django authorization forms

# Create your views here.


#user registration
class RegisterUser(CreateView):
    django_form = UserCreationForm
    template = 'signup_page.html' 
    user_created = reverse_lazy('login')

#user profile
class UserProfile(DetailView):
    model = User
    template = 'profile.html'
    context_object = 'profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])



# Create your views here.
