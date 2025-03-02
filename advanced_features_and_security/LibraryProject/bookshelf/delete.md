```python
# Delete Operation
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
all_books = Book.objects.all()
print(all_books)

# Expected Output:
# <QuerySet []>