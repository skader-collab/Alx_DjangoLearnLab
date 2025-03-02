import os
import django
from django.core.exceptions import ObjectDoesNotExist

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_of_library(library_name):
     try:
        library = Library.objects.get(name=library_name)
        return library.librarian if library.librarian else "No librarian assigned."
     except ObjectDoesNotExist:
         return f"Library '{library_name}' not found."
def get_librarian_of_library(library_name):
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        return librarian
    except ObjectDoesNotExist:
        return f"No librarian found for library '{library_name}'."
    

if __name__ == "__main__":
    # Example Usage
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_of_library("Central Library"))
