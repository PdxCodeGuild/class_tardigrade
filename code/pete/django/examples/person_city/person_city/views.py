from django.shortcuts import render

from .models import City

def index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    # for city in cities:
    #     print()
    #     print(city.name)
    #     for person in city.people.filter(name='Alnardo'):
    #         print(person)
    return render(request, 'index.html', context)