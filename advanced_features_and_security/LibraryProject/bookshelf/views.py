from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from . models import Book

# Create your views here.
@permission_required('myapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('myapp.can_create', raise_exception=True)
def book_create(request):
    # Handle book creation logic
    pass

@permission_required('myapp.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Handle book editing logic
    pass

@permission_required('myapp.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    # Redirect after deletion
    pass
