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
    
    def

