from lib2to3.pytree import Base
from django.core.management.base import BaseCommand

from states.models import State

class Command(BaseCommand):
    help = 'Loads states from csv file'

    def handle(self, *args, **options):
        with open('data/states.csv', 'r') as f:
            data = f.read().split('\n')[1:]
        print(data)
        for line in data:
            line = line.split(',')
            State.objects.get_or_create(name=line[0], abbreviation=line[1])