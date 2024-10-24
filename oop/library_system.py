class Book:
    def __init__(seld,title,author):
        self.title = title
        self.author = author

     def get_details(self):
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    def __init__(self,title,auhtor,file_size):
        super().__init_(author,title)
        self.file_size = file_size
    def get_details(self):
        return f"{super().get_details()}, File Size: {self.file_size}MB"
  


class Print_Book(Book):
    def __init__(self, tile, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def get_details(self):
        # Override get_details method to include file_size
        return f"{super().get_details()}, Page Count: {self.page_count}"

class library:
    self.books = []
    def add_book(self,book):
        self.books.append(book)
        def list_books(self):
        
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book.get_details())

