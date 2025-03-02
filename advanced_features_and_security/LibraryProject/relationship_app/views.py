from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import BookForm  # Assuming you have a BookForm

# Create your views here.
''' function based view '''
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
    

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Custom LoginView to use our login.html template
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Custom LogoutView to use our logout.html template
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


def is_admin(user):
    if user.is_authenticated:
        try:
            return user.userprofile.role == 'Admin'
        except UserProfile.DoesNotExist:
            return False
    return False

def is_librarian(user):
    if user.is_authenticated:
        try:
            return user.userprofile.role == 'Librarian'
        except UserProfile.DoesNotExist:
            return False
    return False

def is_member(user):
    if user.is_authenticated:
        try:
            return user.userprofile.role == 'Member'
        except UserProfile.DoesNotExist:
            return False
    return False

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace 'book_list' with your book list view name
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list') # Replace 'book_list' with your book list view name
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list') # Replace 'book_list' with your book list view name
    return render(request, 'relationship_app/delete_book.html', {'book': book})