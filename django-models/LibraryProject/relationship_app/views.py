from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Create your views here.
''' function based view '''
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

''' class based view '''
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"