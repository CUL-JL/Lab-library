class CircularNode:
    def __init__(self, data):
        self.data = data   
        self.next = None  

class CircularList:
    def __init__(self):
        self.head = None  

    def add_list(self, data):
        new_node = CircularNode(data)
        if self.head:  
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next, new_node.next = new_node, self.head
            return
        
        self.head = new_node
        new_node.next = self.head

    def show_list(self):
        if not self.head:
            print("La lista está vacía.")
            return
        
        last_node = self.head
        while True:
            print(f"- {last_node.data}")
            last_node = last_node.next
            if last_node == self.head:
                break