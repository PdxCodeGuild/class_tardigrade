from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    slug = models.SlugField()

    def __str__(self):
        return self.abbreviation

# all people in a given State object: state.people.all()

class Person(models.Model):
    name = models.CharField(max_length=50)
    # many-to-one relationship 
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='people')
    # without related_name='people' kwarg, you would get the people with that state via:
    # state.person_set.all(), but with the kwarg, you cna just state.people.all()
    lived_in_states = models.ManyToManyField(State, related_name='one_time_residents')

    def __str__(self):
        return self.name

# a Person object's state: person.state