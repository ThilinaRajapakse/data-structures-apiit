class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def insert_front(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node


list_1 = LinkedList()
print(list_1.is_empty())

list_1.insert_front(Node(data=5))
list_1.insert_front(Node(data=3))
print(list_1.is_empty())

list_1.traverse()

