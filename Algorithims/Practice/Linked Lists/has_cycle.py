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

        while current is not None and current != data:
            previous = current
            current = current.next
        
        if current is None:
            return
        
        previous.next = current.next



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

        if self.head == data:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current is not None and current != data:
            previous = current
            current = current.next
        
        if current is None:
            return
        
        previous.next = current.next


def has_cycle(head):
    nodes = set()
    curr_node = head
    while curr_node != None:
        if curr_node in nodes:
            return True   
        nodes.add(curr_node)
        curr_node = curr_node.next 
    return False

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(has_cycle(ll.head))

ll.head.next.next.next.next = ll.head.next
print(has_cycle(ll.head))

ll1 = LinkedList()
ll1.append(1)
print(has_cycle(ll1.head))  # Expected: False

ll2 = LinkedList()
ll2.append(1)
ll2.head.next = ll2.head
print(has_cycle(ll2.head))  # Expected: True

ll3 = LinkedList()
ll3.append(1)
ll3.append(2)
ll3.append(3)
ll3.append(4)
ll3.append(5)
ll3.append(6)
print(has_cycle(ll3.head))  # Expected: False

ll4 = LinkedList()
ll4.append(1)
ll4.append(2)
ll4.append(3)
ll4.append(4)
ll4.append(5)
ll4.head.next.next.next.next.next = ll4.head
print(has_cycle(ll4.head))  # Expected: True



def has_cycle_2(head):
    tort, hare = head, head

    
    while hare and hare.next:
        tort, hare = tort.next, hare.next.next
        if tort == hare:
            tort = head
            while tort != hare:
                tort = tort.next
            return tort.data
    return False

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(has_cycle_2(ll.head))

ll.head.next.next.next.next = ll.head.next
print(has_cycle_2(ll.head))

ll1 = LinkedList()
ll1.append(1)
print(has_cycle_2(ll1.head))  # Expected: False

ll2 = LinkedList()
ll2.append(1)
ll2.head.next = ll2.head
print(has_cycle_2(ll2.head))  # Expected: True

ll3 = LinkedList()
ll3.append(1)
ll3.append(2)
ll3.append(3)
ll3.append(4)
ll3.append(5)
ll3.append(6)
print(has_cycle_2(ll3.head))  # Expected: False

ll4 = LinkedList()
ll4.append(1)
ll4.append(2)
ll4.append(3)
ll4.append(4)
ll4.append(5)
ll4.head.next.next.next.next.next = ll4.head
print(has_cycle_2(ll4.head))  # Expected: True