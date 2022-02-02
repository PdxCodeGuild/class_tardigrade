from django.forms import ModelForm, TextInput, DateInput

from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        # fields = ('author', 'title', 'publication_date', 'pages')
        fields = '__all__'
        widgets = {
             'title': TextInput(attrs={'class': 'red-border'}),
             'publication_date': DateInput(attrs={'type': 'date'}), # didn't work 🤷‍♀️
        }