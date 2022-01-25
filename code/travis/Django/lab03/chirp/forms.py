from django.forms import ModelForm
from .models import Chirp



class ChirpForm(ModelForm):

     class Meta:


         model = Chirp
         fields = ['title', 'message', ]
