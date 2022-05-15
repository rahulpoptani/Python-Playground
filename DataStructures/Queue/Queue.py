import sys, os
sys.path.append(os.path.abspath(os.curdir))
from DataStructures.Stack.Stack import Stack

class Queue:
    def __init__(self):
        self.list = []
    
    def isEmpty(self):
        return self.list == []
    
    def enqueue(self, item):
        self.list.insert(0,item)
    
    def dequeue(self):
        return self.list.pop()
    
    def size(self):
        return len(self.list)
    
    def printQueue(self):
        print (self.list)
    
    # reverse first k elements of Queue: O(n)
    def reverseK(self, k):
        stack = Stack()
        for _ in range(k):
            stack.push(self.dequeue())
        while stack.isEmpty is False:
            self.enqueue(stack.pop())
        for _ in range(self.size() - k):
            self.enqueue(self.dequeue())