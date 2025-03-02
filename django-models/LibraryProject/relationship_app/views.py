from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

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