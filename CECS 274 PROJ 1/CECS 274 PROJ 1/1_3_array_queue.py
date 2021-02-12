from utils import new_array
from base import BaseSet

class ArrayQueue:

    
    def __init__(self):
        self.a = new_array(1) 
        self.size = 0
        self.cap = len(self.a)
        self.front = 0
        self.empty = 0
    
    def dequeue(self): #to remove an element from the Array
        if self.size == 0:
            print("Queue is empty.")
        else:
            print(self.a[self.front%self.cap])
        self.a[self.front%self.cap]
        self.front += 1
        self.size -= 1

    def enqueue(self, e): #To add an element form the Array
        if self.size == self.cap:
            self._resize(2 * self.cap)
        self.empty = (self.front + self.size) % self.cap
        self.a[self.empty] = e
        self.size += 1
        
    def _resize(self, cap): #Resize the Array list
       b = new_array(cap)
       for i in range(self.size):
           b[i] = self.a[(self.front + i) % self.size]
       self.a = b
       self.cap = cap
       self.front = 0
            
queue = ArrayQueue()
queue.dequeue()  # it prints “Queue is empty”
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue() # it returns 1
queue.enqueue(4)
queue.dequeue() # it returns 2 
queue.dequeue() # it returns 3
queue.enqueue(5)
queue.dequeue() # it returns 4
queue.dequeue() # it returns 5
queue.dequeue() # it prints “Queue is empty”


