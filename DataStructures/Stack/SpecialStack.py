from Stack import Stack

class SpecialStack(Stack):
    def __init__(self):
        super().__init__()
        self.min = Stack()
    
    def push(self, data):
        if self.isEmpty():
            super().push(data)
            self.min.push(data)
        else:
            super().push(data)
            y = self.min.pop()
            self.min.push(y)
            if data <= y:
                self.min.push(data)
            else:
                self.min.push(y)
    
    def pop(self):
        x = super().pop()
        self.min.pop()
        return x
    
    def getMin(self):
        x = self.min.pop()
        self.min.push(x)
        return x
    
    def peek(self):
        if self.top == -1: return
        return self.array[self.top]