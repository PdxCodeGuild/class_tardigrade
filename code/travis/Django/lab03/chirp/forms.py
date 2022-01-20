

from django import forms
class PostForm(forms.Form):



    contact_name = forms.CharField(label='Contact Name', max_length=100)
    contact_age = forms.IntegerField(label='Contact Age')