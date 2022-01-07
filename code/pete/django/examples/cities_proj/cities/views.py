from django.shortcuts import render

from .models import City

def index(request):
    # look at index.html, when a form is submitted with method="POST",
    # request.method will be 'POST'
    if request.method == 'POST':
        # print(request.POST) # request.POST is a QueryDict, a dictionary-like object
        # where the name attributes of inputs are the keys and the values of those input
        # elements are the values
        name_input = request.POST.get('name')
        country_input = request.POST.get('country')
        food_input = request.POST.get('food')
        population_input = request.POST.get('population')
        # Model.objects.create will create a new object in the database
        # name=name is a keyword argument (kwarg), so are the rest of these
        # it is instantiating a City object with these kwargs and saving it to the database
        City.objects.create(name=name_input, country=country_input, food=food_input, population=population_input)

    cities = City.objects.all() # a QuerySet of all City objects from the database
    context = {'cities': cities} # the context dictionary
    return render(request, 'cities/index.html', context)