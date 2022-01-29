import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import ChirpForm
from .models import Chirp
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def main(request):

    chirp_list = Chirp.objects.all().order_by("-post_date")

    context = {'chirp_list': chirp_list}

    return render(request, 'chirp/index.html', context)


@login_required
def submit(request):

    if request.user.is_authenticated:

        if request.method == 'POST':

            form = ChirpForm(request.POST)

            if form.is_valid():

                username = User.objects.get(username=request.user.username)
                post_date = datetime.datetime.now()
                title = form.cleaned_data["title"]
                message = form.cleaned_data["message"]

                new_chirp = Chirp.objects.create(
                    username=username, title=title, message=message, post_date=post_date)
                new_chirp.save()

                return redirect("/")
        else:

            form = ChirpForm()

    else:

        return redirect("/submit")

    return render(request, 'chirp/submit.html', {'form': form})
