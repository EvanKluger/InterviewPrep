class Stack:

    def __init__(self):
        self.items = []
    
    def pop(self):
        if self.empty():
            self.items.pop()
        else:
            return None
    
    def push(self,item):
        self.items.append(item)
    
    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.empty():
            return None
        else:
            return self.items[-1]