
class TwoStack():
    def __init__(self, n):
        self.size = n
        self.array = [None] * n
        self.top1 = -1
        self.top2 = self.size
    
    def push1(self, x):
        # there should be atleast one empty space for the new element
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.array[self.top1] = x
        else:
            print('Stack Overflow')
            return
    
    def push2(self, x):
        if self.top1 < self.top2-1:
            self.top2 -= 1
            self.array[self.top2] = x
        else:
            print('Stack Overflow')
            return
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.array[self.top1]
            self.top1 -= 1
            return x
        else:
            print('Stack Underflow')
            return
    
    def pop2(self):
        if self.top2 < self.size:
            x = self.array[self.top2]
            self.top2 += 1
            return x
        else:
            print('Stack Underflow')
            return
    
    def printStack(self):
        print(self.array)
