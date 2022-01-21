from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        posts = request.user.chirps.all()
        context = {'posts' : posts}
        return render(request, 'chirp/index.html', context)
    return render(request, 'chirp/index.html')

def add(request):
    title_input = request.POST.get('title')
    chirp_input = request.POST.get('chirp')
    Post.objects.create(title=title_input, chirp=chirp_input, user=request.user)
    return redirect('/')