from .models import Post
from .forms import CommentForm
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

def index(request):
    posts = Post.objects.order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def post(request):
    if request.method == 'POST':
        post = request.POST.get('post')
        Post.objects.create(
            post=post,
            user=request.user
        )
        return redirect('posts:index')

    return render(request, 'posts/index.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'posts/postdetail.html', {'post': post,
                                                      'comments': comments,
                                                      'new_comment': new_comment,
                                                      'comment_form': comment_form})

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:index')

# class UpdatePostView(UpdateView):
#     model = Post
#     template_name = 'editpost.html'
#     fields = ['title', 'post']




