from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, CustomLogoutView, CustomLoginView, register

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-Based View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
