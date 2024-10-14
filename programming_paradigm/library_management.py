class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book and set it as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return the availability status of the book."""
        return not self._is_checked_out


class Library:
    """A class representing a library that holds a collection of books."""
    
    def __init__(self):
        """Initialize an empty library with a list of books."""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.check_out():
                return f"You have checked out '{title}'."
        return f"'{title}' is not available for checkout."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.return_book():
                return f"You have returned '{title}'."
        return f"'{title}' was not checked out."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if book.is_available()]
        return available_books if available_books else "No available books."
