from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
        # Filtering
    filterset_fields = ['title', 'author', 'publication_year']
    
    
    search_fields = ['title', 'author']
    

    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  
    

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only staff members can add books.")
        serializer.save()

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only staff members can edit books.")
        serializer.save()

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

