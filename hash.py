class Hash:

    def __init__(self, size=1009):
        self.table = [None] * size
        
        self.curr_size = size
        self.num_items = 0

        self.primes = [
        2027, 4079, 8171, 16369, 32749, 65521, 131071, 262139, 524287, 
        1048573, 2097143, 4194301, 8388593, 16777213, 33554393, 67108859, 
        134217689, 268435399, 536870909, 1073741789, 2147483647
    ]
    
    def insert(self, val):
        val_idx = self.hash(val)

        if self.num_items / self.curr_size > 0.5:
            self.resize()

        if self.table[val_idx] == None:
            self.table[val_idx] = val
            self.num_items += 1
            return
        
        else:
            start = val_idx
            i = start+1
            while i != start:
                if self.table[i] == None:
                    self.table[i] = val
                    #val added
                    self.num_items += 1
                    return
                i += 1
                if i == self.curr_size:
                    i = 0
            self.resize()
            self.insert(val)
            return

    def delete(self,val):
        del_idx = self.hash(val)
        if self.table[del_idx] == val:
            self.table[del_idx] = None
            self.num_items -= 1
            #Deleted Val
            return
        else:
            if self.table[del_idx] == None:
                #Value not in Table
                return
            else:
                start = del_idx
                i = start+1
                while i != start:
                    if self.table[i] == val:
                        self.table[i] = None
                        #del val
                        self.num_items -= 1
                        return
                    i += 1
                    if i == self.curr_size:
                        i = 0
                #Value not in table
                return

    def lookup(self,val):
        lookup_idx = self.hash(val)
        if self.table[lookup_idx] == val:
            #Value Found
            return val
        else:
            if self.table[lookup_idx] == None:
                return None
            else:
                start = lookup_idx
                i = start+1
                while i != start:
                    if self.table[i] == val:
                        return val
                    i += 1
                    if i == self.curr_size:
                        i = 0
                return None
    
    def hash(self, val):
        return val % len(self.table)
    
    def resize(self):
        old_table = self.table
        self.curr_size = self.primes.pop(0)
        self.table = [None] * self.curr_size

        for item in old_table:
            if item is not None:
                self.insert(item)
        
