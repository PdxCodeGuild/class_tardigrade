from functools import _Descriptor
from django import forms


class GroceryForm(forms.Form):

    description = forms.CharField(label='description', max_length=50)
    created_date = forms.DateTimeField()
    completed_date = forms.DateTimeField(null=True, blank=True)
    completed = forms.BooleanField(default=False)


    def __str__(self):
        return self.description