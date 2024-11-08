from modules.simple_list import simple_list
from modules.double_list import DoubleList
from modules.circular_list import CircularList

# Super class for all controllers
class LibraryControllers:
        def __init__(self, arrival_books, alphabetically_books, recommended_books):
            self.__arrival_books = arrival_books
            self.__alphabetically_books = alphabetically_books
            self.__recommended_books = recommended_books

class Book(LibraryControllers):
    def __init__(self, Title, author, year_publication, recommended):
        self.title = str(Title)
        self.author = str(author)
        self.year_publication = str(year_publication)
        self.__recommended = int(recommended)