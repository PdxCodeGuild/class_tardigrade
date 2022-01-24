from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import User_Info, Post

def index(request):
    if request.user.is_authenticated:
        return redirect('posts:home')
    else:
        return render(request, 'posts/index.html')

def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'posts/home.html', context)

@require_http_methods(['POST'])
def make_post(request):
    if request.method == 'POST':
        content = request.POST.get("content")
        user = request.user.username
        user = User_Info.objects.filter(user_name=user).get()
        Post.objects.create(content=content, user=user)
    return redirect('posts:home')

@require_http_methods(['POST'])
def delete(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)
    post.delete()
    return redirect('posts:home')