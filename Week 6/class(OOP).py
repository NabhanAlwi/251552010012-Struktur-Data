from collections import deque

class queue:
    def __init__(self):
        self.item = deque()
        
    def enqueue(self, item):
        self.item.append(item)
    
    def dequeue (self):
        if not self.is_empty():
            return self.items.popleft()
        return 'queue kosong!'
    
    def peek(self):
        if not self.is_empty():
            return self.item[0]
        
    def is_empty(self): return len(self.items) ==0
    def size(self): return len (self.items)
    def __str__(self): return str(list(self.items))