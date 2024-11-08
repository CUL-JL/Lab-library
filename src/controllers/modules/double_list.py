class DobleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = DobleNode(data)
        if self.head:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next, new_node.prev = new_node, last_node
            return
        self.head = new_node

    def alphabetic_order(self):
        if self.head:
            change = True
            while change:
                change, node = False, self.head
                while node.next:
                    if node.data > node.next.data:
                        node.data, node.next.data, change = node.next.data, node.data, True
                    node = node.next

    def show_list(self):
        last_node = self.head
        while last_node:
            if last_node.next:
                print(last_node.data, end=", ")
            else:
                print(last_node.data)
            last_node = last_node.next