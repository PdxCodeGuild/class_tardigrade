from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Posts
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
#import django authentication

class PostList(ListView):  #lists posts
    model = Posts
    html ='home.html'

class PostDetail(DetailView): #individual post display
    model = Posts
    html = 'detail_page.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Posts
    html = 'new_post_page.html' #create new post display
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    html = 'edit_post_page.html'
    fields = ['title', 'body']

    def test_func(self): #edit post  and return  post
        post = self.get_object() 
        return self.request.user == post.user

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    html = 'delete_post_page.html' #delete post class
    pass_url = reverse_lazy('posts:home') 

    def test_func(self):  #checks user
        post = self.get_object()
        return self.request.user == post.user




# Create your views here.
