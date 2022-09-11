from dataclasses import field
from random import choices
from django import forms
from main.models import Author, Book, UserList, Reviews
from django.forms import ModelForm


class CreateNewAuthor(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': 'Author Name:',
            'born': 'Birth Date:',
            'about': 'About Author:',
            'portrait_url': 'Portrait URL:',
        }
        widgets = {
            'born': forms.DateInput(attrs={'type': 'date'}),
            'about': forms.Textarea(attrs={'type': 'textarea', 'rows': 10, 'placeholder': 'up to 2000 chars'}),
            'portrait_url': forms.URLInput(attrs={'type': 'url'}),
        }
    
    
class CreateNewBook(ModelForm):

    class Meta:
        model = Book
        fields = ['author','book_name', 'pub_date', 'num_pages', 'cover_url', 'pdf_url', 'summary']
        labels = {
            'author': 'Author:',
            'book_name': 'Book Name:',
            'pub_date': 'Pub Date:',
            'num_pages': 'Num Pages:',
            'cover_url': 'Book Cover URL:',
            'pdf_url': 'Book PDF URL:',
        }
        widgets = {
            'author': forms.Select,
            'book_name': forms.TextInput(attrs={'type': 'text'}),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'cover_url': forms.URLInput(attrs={'type': 'url'}),
            'pdf_url': forms.URLInput(attrs={'type': 'url'}),
            'summary': forms.Textarea(attrs={'type': 'textarea', 'rows': 5, 'placeholder': 'up to 2000 chars'}),
        }
        

class CreateUserList(ModelForm):
    
    class Meta:
        model = UserList
        fields = ('list_name',)
        labels = {
            'list_name': "name of new list:"
        }
        

class CreateReview(ModelForm):
    
    class Meta:
        model = Reviews
        exclude = ['owner', 'book', ]
        