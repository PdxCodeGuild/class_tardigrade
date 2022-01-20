from django.shortcuts import render
from django.http import HttpResponse

def firsttest(request):
    return HttpResponse('ok')

# def firsttest(request):
#     context = {
#         something = <model/something>
#         }
#     return render(request, 'chirp/index.html', context)


