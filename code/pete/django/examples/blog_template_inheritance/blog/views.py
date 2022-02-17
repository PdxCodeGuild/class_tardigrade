from webbrowser import get
from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def post(request, id):
    context = {
        'post': get_object_or_404(Post, id=id)
    }
    return render(request, 'blog/post.html', context)