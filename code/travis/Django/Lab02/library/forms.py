from django import forms
from .models import CheckoutBook 


# Create your forms here.
class CheckoutForm(forms.ModelForm):

    class Meta:
        model = CheckoutBook
       # fields = ('title', 'user', 'is_checked_out', 'time_stamp')
        fields = ('user',)