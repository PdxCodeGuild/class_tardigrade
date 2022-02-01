
from email import message
from django.forms import ModelForm, Textarea, widgets
from .models import Chirp

class ChirpForm(ModelForm):


    class Meta:

         model = Chirp

         fields = ['title', 'message']
         widgets = { "message": Textarea(attrs={"cols":30, "rows": 12})}
