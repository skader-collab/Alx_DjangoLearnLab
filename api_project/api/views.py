from django.shortcuts import render
from rest_framework.generics.ListAPIView import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission


# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Librarians').exists()

# Book API viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated, IsLibrarian]  