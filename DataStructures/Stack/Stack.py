class Stack:
    def __init__(self):
        self.list = []
        self.top = -1
        self.max = 100
    
    @property
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.max - 1
    
    def push(self, data):
        if self.isFull():
            print('Stack Overflow')
            return
        else:
            self.top += 1
            self.list.append(data)
    
    def pop(self):
        if self.isEmpty:
            print('Stack Underflow')
            return
        else:
            self.top -= 1
            return self.list.pop()
    
    def peek(self):
        if not self.isEmpty:
            return self.list[self.top]
    
    def size(self):
        return self.top
    
    def printStack(self):
        if self.top == -1: return
        print(self.list)
