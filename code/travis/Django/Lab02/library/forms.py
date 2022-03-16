from django import forms
from .models import Book 


class CheckoutForm(forms.ModelForm):
    user = forms.CharField(label=False)
    
    class Meta:        
        model = Book

        fields = ('user',)