from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        posts = request.user.chirps.all()
        all_posts = Post.objects.all()
        context = {'posts' : posts,
                    'all_posts': all_posts}
        return render(request, 'chirp/index.html', context)
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'chirp/index.html', context)

def add(request):
    title_input = request.POST.get('title')
    chirp_input = request.POST.get('chirp')
    Post.objects.create(title=title_input, chirp=chirp_input, user=request.user)
    return redirect('/')