
from django.forms import ModelForm
from .models import User

class UserLoginForm(ModelForm):
    class Meta:
        # the model to associate with the form
        model = User
  
        fields = ['user, password']




  
