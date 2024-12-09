
# University Library System
# Purpose: This script implements a library management system for a university.

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __repr__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book(ISBN: {self.isbn}, Title: '{self.title}', Author: '{self.author}', Status: {status})"

class Library:
    def __init__(self):
        self.books_by_isbn = {}  # Dictionary for fast lookup by ISBN
        self.sorted_books = []  # List for sorted view of books (by title)

    def add_book(self, isbn, title, author):
        if isbn in self.books_by_isbn:
            print("Book with this ISBN already exists.")
            return
        book = Book(isbn, title, author)
        self.books_by_isbn[isbn] = book
        self.sorted_books.append(book)
        self.sorted_books.sort(key=lambda b: b.title)  # Keep books sorted by title
        print(f"Book '{title}' added successfully.")

    def search_by_title(self, title):
        low, high = 0, len(self.sorted_books) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.sorted_books[mid].title.lower() == title.lower():
                return self.sorted_books[mid]
            elif self.sorted_books[mid].title.lower() < title.lower():
                low = mid + 1
            else:
                high = mid - 1
        return None

    def search_by_isbn(self, isbn):
        return self.books_by_isbn.get(isbn, None)

    def borrow_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book:
            if book.is_borrowed:
                print(f"Book '{book.title}' is already borrowed.")
            else:
                book.is_borrowed = True
                print(f"Book '{book.title}' borrowed successfully.")
        else:
            print("Book not found.")

    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book:
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"Book '{book.title}' returned successfully.")
            else:
                print(f"Book '{book.title}' was not borrowed.")
        else:
            print("Book not found.")

    def display_books(self):
        if not self.sorted_books:
            print("No books available in the library.")
        else:
            print("Library Collection:")
            for book in self.sorted_books:
                print(book)


# Example test cases to demonstrate the functionality
if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    library.add_book("978-0132350884", "Clean Code", "Robert C. Martin")
    library.add_book("978-0201616224", "The Pragmatic Programmer", "Andrew Hunt")
    library.add_book("978-0262033848", "Introduction to Algorithms", "Thomas H. Cormen")

    # Display all books
    print("\nAll books in the library:")
    library.display_books()

    # Test Case 1: Search for a book by title
    print("\nSearch by title:")
    book = library.search_by_title("Clean Code")
    if book:
        print(f"Found: {book}")
    else:
        print("Book not found.")

    # Test Case 2: Borrow a book
    print("\nBorrowing a book:")
    library.borrow_book("978-0132350884")

    # Test Case 3: Attempt to borrow the same book again
    print("\nBorrowing the same book again:")
    library.borrow_book("978-0132350884")

    # Test Case 4: Return a book
    print("\nReturning a book:")
    library.return_book("978-0132350884")

    # Test Case 5: Search for a non-existent book
    print("\nSearch for a non-existent book:")
    book = library.search_by_title("Non-existent Book")
    if book:
        print(f"Found: {book}")
    else:
        print("Book not found.")

    # Test Case 6: Display all books after borrowing and returning
    print("\nUpdated Library Collection:")
    library.display_books()
