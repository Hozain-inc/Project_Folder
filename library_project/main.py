
from My_data import data
from utils import helpers
from services import library

# To add some books
data.add_book("Python Basics", "John Doe")
data.add_book("Advanced Python", "Jane Smith")

# To display all books
print("Library Collection:")
for b in data.get_books():
    print(helpers.format_book(b))

# To borrow a book
print("\nBorrowing a book:")
print(library.borrow_book("Python Basics"))

# To display books again
print("\nUpdated Library Collection:")
for b in data.get_books():
    print(helpers.format_book(b))