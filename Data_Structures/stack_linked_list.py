class LinkedList:

    def __init__(self):
        self.head = None
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def append(self, data):
        new_node = self.Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert(self, data, position):
        new_node = self.Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(position -1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, data):
        if self.head ==  None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current is not None and current.data != data:
            previous = current
            current = current.next
        
        if current is None:
            return
        
        previous.next = current.next


class Stack_ll:

    def __init__(self):
        self.items = LinkedList()
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            pop_value = self.items.head.data
            self.items.head = self.items.head.next
            return pop_value

    def push(self, data):
        return self.items.insert(data, 0)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items.head.data
         
    
    def is_empty(self):
        return self.items.head is None
    