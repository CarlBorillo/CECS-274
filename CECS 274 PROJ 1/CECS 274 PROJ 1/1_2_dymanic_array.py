from utils import new_array


class DynamicArray:

    def __init__(self):
        self.a = new_array(1) #New array is created
        self.n = 0 #Number of elements in the array
        self.capacity = len(self.a) #The capacity of the array

    def resize(self, capacity, k, value):
        b = new_array(capacity) #New array created
        index = 0 #the index is tracked
        for i in range(self.n + 1):
            if i == k: #k is is specified index, adds an element
                b[i] = value
            else:
                b[i] = self.a[index]
                index += 1
        self.a = b
        self.capacity = capacity

    def insert(self, k, value): #Inserts an element
        if self.n == self.capacity:
            self.resize(2 * self.capacity, k, value)
            
        else:
            for j in range(self.n, k, - 1):
                self.a[j] = self.a[j - 1]
            self.a[k] = value
        self.n += 1

    def __str__(self): #prints out the output
        s = "["
        for i in range(self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        s += "]"
        return s

dynamic_array = DynamicArray()
dynamic_array.insert(0,1)
dynamic_array.insert(0,2)
dynamic_array.insert(1,3)
dynamic_array.insert(3,5)
dynamic_array.insert(2,4)
print(dynamic_array) # it prints [2,3,4,1,5]

