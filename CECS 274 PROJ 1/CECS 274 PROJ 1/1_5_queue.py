# add is O(1) because it appends which doesnt take any time.
# Remove is O(1) because if stack_1 is empty, returns empty queue
# It appends popped values from stack_1 to stack_2 and returns popped value of stack_2
class QueueStack: 

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def add(self, item): #adds item to stack
        self.stack_1.append(item)
        return (self.stack_1)
        

    def remove(self): #will remove item from stack
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            print("Queue is empty")
        else:
            if len(self.stack_2) == 0 and len(self.stack_1) > 0:
                while len(self.stack_1) > 0:
                    self.stack_2.append(self.stack_1.pop())
            print(self.stack_2.pop())    


queue = QueueStack()

queue.remove()
queue.add(1)
queue.add(2)
queue.add(3)
queue.remove()
queue.add(4)
queue.remove()
queue.remove()
queue.add(5)
queue.remove()
queue.remove()
queue.remove()
# it prints “Queue is empty”
# it returns 1
# it returns 2 # it returns 3
# it returns 4
# it returns 5
# it prints “Queue is empty”       

