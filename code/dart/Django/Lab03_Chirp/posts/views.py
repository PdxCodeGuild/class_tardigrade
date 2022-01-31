from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chirp, Chirp_comments

def index(request):
    chirps = Chirp.objects.order_by('-created_at')
    context = {
        'chirps': chirps,
    }
    return render(request, 'posts/index.html', context)

@login_required
def chirp(request):
    if request.method == 'POST':
        chirp = request.POST.get('chirp')
        Chirp.objects.create(
            chirp=chirp,
            user=request.user
        )

        return redirect('posts:index')

    return render(request, 'posts/index.html')

@login_required
def chirp_comments(request, id):
    if request.method == 'POST':
        comment = request.POST.get('reply')
        Chirp_comments.objects.create(
            comment=comment,
            user=request.user
        )
    chirp = get_object_or_404(Chirp, id=id)
    context = {
        'chirp': chirp,
    }
    return render(request, 'posts/chirp.html', context)

@login_required
def likes(request, id):
    like = get_object_or_404(Chirp, id=id)
    like.likes.add(request.user)
    return redirect('posts:index')

@login_required
def delete(request, id):
    chirp = get_object_or_404(Chirp, id=id)
    chirp.delete()
    return redirect('posts:index')