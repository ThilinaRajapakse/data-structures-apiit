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

    def insert_front(self, node):
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            