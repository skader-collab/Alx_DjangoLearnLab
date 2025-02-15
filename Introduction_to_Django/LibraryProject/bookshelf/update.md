```python
# Update Operation
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
updated_book = Book.objects.get(pk=book.id)
print(updated_book.title)

# Expected Output:
# 'Nineteen Eighty-Four'