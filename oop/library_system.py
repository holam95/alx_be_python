class Book:
    def __init__(seld,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    def __init__(self,title,auhtor,file_size):
        super().__init_(author,title)
        self.file_size = file_size
    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size}MB"
  


class PrintBook(Book):
    def __init__(self, tile, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        # Override get_details method to include file_size
        return f"{super().__str__()}, Page Count: {self.page_count}"

class library:
    self.books = []
    def add_book(self,book):
        self.books.append(book)
        def list_books(self):
        # Print details of all books in the library
            if not self.books:
                print("No books in the library.")
            else:
                for book in self.books:
                    print(book.get_details())

