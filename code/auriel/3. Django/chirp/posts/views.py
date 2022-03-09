from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Post, User
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        print(request.POST) 
        data = dict(request.POST)
        print(data)
        chirp = request.POST.get('words')
        Post.objects.create(
			chirp = chirp,
			time = datetime.now(),
            author = request.user,
		)
        return redirect('/')

    context={'posts':(Post.objects.all()),}
    print(context)
    return render(request, 'posts/home.html', context)

@login_required
def delete(request, id):
    item = get_object_or_404(Post, id=id)
    item.delete()
    return redirect('posts:home')

@login_required
def profile(request, id):
    if request.method == 'POST':
        print(request.POST) 
        data = dict(request.POST)
        print(data)
        chirp = request.POST.get('words')
        Post.objects.create(
			chirp = chirp,
			time = datetime.now(),
            author = request.user,
		)
        return redirect('/user')
        
    user=get_object_or_404(User, id=id)
    context={'posts':(Post.objects.filter(author=user.id))}
    return render(request, 'posts/user.html', context)