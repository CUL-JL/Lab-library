class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class DobleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

class CircularNode(Node):
    def __init__(self, data):
        super().__init__(data)