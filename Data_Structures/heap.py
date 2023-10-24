class Heap:

    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        
        self.heap.append(value)
        self.heapify_up(self.size() - 1)


    def extract_min(self):
        if self.is_empty():
            return None
        
        return_val = self.heap[0]
        self.heap[0], self.heap[self.size()-1] = self.heap[self.size()-1], self.heap[0]
        self.heap.pop()
        self.heapify_down(0)
        return return_val 

    def peek_min(self):
        
        if self.is_empty():
            return None
        
        return self.heap[0]
          

    def heapify_down(self, index):
                
        curr_index = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        while left_child < self.size():
            swap_index = left_child
            if right_child < self.size() and self.heap[right_child] < self.heap[left_child]:
                swap_index = right_child

            if self.heap[curr_index] > self.heap[swap_index]:
                self.heap[curr_index], self.heap[swap_index] = self.heap[swap_index], self.heap[curr_index]
                curr_index = swap_index
                left_child = 2 * curr_index + 1
                right_child = 2 * curr_index + 2
            
            else:
                break
        return 

            

    def heapify_up(self, index):
        while index != 0 and self.heap[(index-1)//2] > self.heap[index]:
            self.heap[(index-1)//2], self.heap[index] = self.heap[index], self.heap[(index-1)//2]
            index = (index - 1) // 2 

        
    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.heap) 
   

