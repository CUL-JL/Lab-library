from book import Book
from node import SimpleList

class LibraryController:
    def __init__(self):
        self.simple_list = SimpleList()

    def add_book(self, title, author, year, recommendation):
        book = Book(title, author, year, recommendation)
        self.simple_list.add_book(book)

    def search_book(self, title):
        return self.simple_list.search_title(title)

    def delete_book(self, title):
        return self.simple_list.delete_book(title)

    def show_books(self):
        return self.simple_list.show_books()
