import sys, os
sys.path.append(os.path.abspath(os.curdir))
from DataStructures.Stack.Stack import Stack

class QueueList:
    def __init__(self):
        self.list = []
        self.qsize = 0
    
    # Time O(1)
    def isEmpty(self):
        return self.qsize == 0
    
    # Time O(1)
    def enqueue(self, item):
        self.qsize += 1
        self.list.insert(0,item)
        return True
    
    # Time O(1)
    def dequeue(self):
        self.qsize -= 1
        return self.list.pop()
    
    # Time O(1)
    def size(self):
        return self.qsize
    
    # Time O(n)
    def printQueue(self):
        print ('Queue: {}'.format(self.list))
    
    # Time O(1)
    def front(self):
        return self.list[self.qsize - 1]
    
    # Time O(1)
    def rear(self):
        return self.list[0]
    
    # reverse first k elements of Queue: O(n)
    def reverseK(self, k):
        stack = Stack()
        for _ in range(k):
            stack.push(self.dequeue())
        while not stack.isEmpty:
            self.enqueue(stack.pop())
        for _ in range(self.size() - k):
            self.enqueue(self.dequeue())
        # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        # [10, 9, 8, 7, 6]
        # [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
        # [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
    
    