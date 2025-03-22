from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Book


class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test data and API client."""
        self.client = APIClient()
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2021)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2022)
        self.book_list_url = reverse('book-list')  # Ensure you have named your BookListView URL as 'book-list'

    def test_list_books(self):
        """Test retrieving list of books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """Test creating a new book."""
        data = {"title": "New Book", "author": "New Author", "publication_year": 2023}
        response = self.client.post(self.book_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating a book."""
        update_url = reverse('book-detail', kwargs={'pk': self.book1.pk})  # Ensure 'book-detail' is your Book detail URL
        updated_data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2024}
        response = self.client.put(update_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book."""
        delete_url = reverse('book-detail', kwargs={'pk': self.book2.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """Test filtering books by author."""
        response = self.client.get(self.book_list_url, {'author': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(self.book_list_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.book_list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')  # Newest book should be first


