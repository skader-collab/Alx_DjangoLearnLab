```python
# Create Operation
from bookshelf.models import Book
new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Expected Output (Django shell response):
# <Book: Book object (1)>