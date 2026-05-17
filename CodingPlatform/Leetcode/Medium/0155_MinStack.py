
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

from Common.Tags import STACK, DESIGN, ARRAY

class MinStack:
    def __init__(self):
        self.list = []
        self.minlist = []
        self.ssize = 0
    
    @property
    def isEmpty(self):
        return self.ssize == 0
    
    def top(self):
        if not self.isEmpty:
            return self.list[-1]

    def push(self, value):
        if self.isEmpty:
            self.ssize += 1
            self.list.append(value)
            self.minlist.append(value)
        else:
            self.ssize += 1
            self.list.append(value)
            if self.minlist[-1] < value:    
                self.minlist.append(self.minlist[-1])
            else:
                self.minlist.append(value)
    
    def pop(self):
        if self.isEmpty: 
            return None
        self.ssize -= 1
        self.minlist.pop()
        return self.list.pop()
    
    # Time O(1)
    def getMin(self):
        if self.isEmpty: 
            return None
        return self.minlist[-1]
    
    def printStack(self):
        if self.ssize == 0: 
            return None
        print('Stack: {} {}'.format(self.list, self.minlist))


ms = MinStack()

ms.printStack()

for x in range(10, 5, -1):
    ms.push(x)

ms.printStack()

print(ms.getMin())

print(f'Pop Element: {ms.pop()}')

ms.printStack()

print(ms.getMin())

print(f'Pop Element: {ms.pop()}')

ms.printStack()

print(ms.getMin())

print(f'Add Element 4: {ms.push(4)}')

ms.printStack()

print(ms.getMin())

