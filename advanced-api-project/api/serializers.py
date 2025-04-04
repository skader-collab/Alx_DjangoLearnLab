from .models import Author, Book
from rest_framework import serializers
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):

        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) 
    class Meta:
        model = Author
        fields = ['name', 'books']