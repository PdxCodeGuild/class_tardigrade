from django.shortcuts import render, get_object_or_404, redirect

from .models import Entry

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Entry.objects.create(title=title, body=body)
        return redirect('/')
        # return redirect('diary:index')



    entries = Entry.objects.all().order_by('-id')
    context = {'entries': entries}
    return render(request, 'diary/index.html', context)

def detail(request, id):
    entry = get_object_or_404(Entry, id=id)
    context = {'entry': entry}
    return render(request, 'diary/entry.html', context)

def update(request, id):
    ...

def delete(request, id):
    ...