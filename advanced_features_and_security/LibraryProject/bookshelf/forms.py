from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title:
            raise forms.ValidationError("Invalid input detected!")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if "<script>" in author:
            raise forms.ValidationError("Invalid input detected!")
        return author
