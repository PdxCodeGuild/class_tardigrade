from django.core.management.base import BaseCommand

import requests

from pokedex.models import Pokemon, Type

class Command(BaseCommand):
    help = 'Calls the pokedex api to save pokemon in the database.'

    def handle(self, *args, **options):
        for i in range(1, 152):
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
            # response.json() gives you a dictionary (if it's a json response)
            data = response.json()
            print(data.keys())
            name = data.get('name') # data['name']
            sprite = data.get('sprites').get('other').get('official-artwork').get('front_default')
            # sprite = data['sprites']['other']['official-artwork']['front_default']
            print(name, sprite)
            pokemon, created = Pokemon.objects.get_or_create(name=name, sprite=sprite)
            if created:
                self.stdout.write(f'{pokemon.name} created')
            types = data.get('types')
            for type in types:
                type = type['type']['name']
                type, created = Type.objects.get_or_create(type=type)
                if created:
                    self.stdout.write(f'{type.type} created')
                pokemon.types.add(type)
            pokemon.save()