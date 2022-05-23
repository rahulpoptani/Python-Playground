import sys, os
sys.path.append(os.path.abspath(os.curdir))
from DataStructures.Stack.Stack import Stack

class QueueStack:
    def __init__(self):
        self.mainStack = Stack()
        self.tempStack = Stack()
    
    # Insert element in Queue
    def enqueue(self, value):
        # Push the value into main stack O(1)
        if self.mainStack.isEmpty and self.tempStack.isEmpty:
            self.mainStack.push(value)
            print('Value: {} inserted in main stack'.format(value))
        else:
            # Insert all elements into temporary stack before making any insertions.
            while not self.mainStack.isEmpty:
                self.tempStack.push(self.mainStack.pop())
            # Insert the value in main stack
            self.mainStack.push(value)
            print('Value: {} inserted in main stack'.format(value))
            # Move all values from temporary stack back to main stack
            while not self.tempStack.isEmpty:
                self.mainStack.push(self.tempStack.pop())
    
    def dequeue(self):
        # if stack empty then return None
        if self.mainStack.isEmpty: return None
        return self.mainStack.pop()
    
    def printQueue(self):
        print('Queue: {}'.format(self.mainStack.list))
