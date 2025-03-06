from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from . models import Book
from .forms import ExampleForm 

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


 # ✅ Import ExampleForm

def search_books(request):
    query = request.GET.get('q', '').strip()

    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'bookshelf/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect after successful submission
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

# ✅ Example view using ExampleForm
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send an email, save to DB)
            return render(request, 'bookshelf/success.html', {'form': form})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})

