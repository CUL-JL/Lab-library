class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SimpleList:
    def __init__(self):
        self.head = None

    def add_book(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search_title(self, title):
        current = self.head
        while current:
            if current.data.title == title:
                return current.data
            current = current.next
        return None

    def delete_book(self, title):
        current = self.head
        prev = None
        while current:
            if current.data.title == title:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current.data
            prev = current
            current = current.next
        return None

    def show_books(self):
        current = self.head
        books = []
        if not current:
            return "No books available."
        while current:
            books.append(str(current.data))
            current = current.next
        return "\n".join(books)