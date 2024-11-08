class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class simple_list:
    def __init__(self):
        self.head = None  # La lista empieza vacía

    def add_list(self, data):
        new_node = Node(data)  # Creamos un nuevo nodo con el data
        if self.head != None:
            # Si la lista no está vacía, recorrer hasta el final y agregar el nodo
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            return
        # Si la lista está vacía, el nuevo nodo es  return
        self.head = new_node

    def show_list(self):
        last_node = self.head
        while last_node:
            # Si el siguiente nodo es None, no se imprime la flecha
            if last_node.next is None:
                return print(last_node.data)  # No agrega " -> " al final
            
            print(last_node.data, end=", ")
            last_node = last_node.next

# Ejemplo de uso
lista = simple_list()
lista.add_list("a")
lista.add_list("b")
lista.add_list("c")
lista.add_list("d")
lista.add_list("e")
lista.show_list()