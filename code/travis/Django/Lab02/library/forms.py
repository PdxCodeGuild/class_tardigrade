from django import forms
from .models import CheckoutBook 


class CheckoutForm(forms.ModelForm):
    user = forms.CharField(label=False)
    
    class Meta:        
        model = CheckoutBook

        fields = ('user',)