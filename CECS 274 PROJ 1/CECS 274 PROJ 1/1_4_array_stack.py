from utils import new_array

from base import BaseList

class ArrayStack(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.a = new_array(1)
        self.n = 0

    def get(self, i): # returns a value in the array
        return self.a[i]

    def add(self, i, x): 
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        self.a[i+1:self.n+1] = self.a[i:self.n]
        self.a[i] = x
        self.n += 1

    def _resize(self):
        b = new_array(max(1, 2*self.n))
        b[0:self.n] = self.a[0:self.n]
        self.a = b
    
    
stack = ArrayStack()
stack.add(0, 1)
stack.add(0, 2)
stack.add(1, 3)
stack.add(3, 5)
stack.add(2, 4)
print(stack.get(0)) # it prints 2
print(stack.get(1)) # it prints 3
print(stack.get(2)) # it prints 4
print(stack.get(3)) # it prints 1
print(stack.get(4)) # it prints 5


