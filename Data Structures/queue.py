class Queue:
    
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def pop(self):
        if self.empty():
            return None
        
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        
        return self.stack_pop.pop()
        
    def push(self, item):
        self.stack_push.append(item)
    
    def empty(self):
        return not self.stack_push and not self.stack_pop
    
    def peek(self):
        if self.empty():
            return None
        
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

        return self.stack_pop[-1]
