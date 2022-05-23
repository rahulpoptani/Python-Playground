class MinStack():
    def __init__(self):
        self.list = []
        self.minlist = []
        self.ssize = 0
    
    @property
    def isEmpty(self):
        return self.ssize == 0
    
    def peek(self):
        if not self.isEmpty:
            return self.list[-1]

    def push(self, value):
        if self.isEmpty:
            self.ssize += 1
            self.list.append(value)
            self.minlist.append(value)
        else:
            if self.minlist[-1] < value:
                self.ssize += 1
                self.list.append(value)
                self.minlist.append(self.minlist[-1])
            else:
                self.ssize += 1
                self.list.append(value)
                self.minlist.append(value)
    
    def pop(self):
        if self.isEmpty: return None
        self.ssize -= 1
        self.minlist.pop()
        return self.list.pop()
    
    # Time O(1)
    def min(self):
        if self.isEmpty: return None
        return self.minlist[-1]
    
    def printStack(self):
        if self.ssize == 0: return None
        print('Stack: {}'.format(self.list))


ms = MinStack()

ms.printStack()

for x in range(10, 5, -1):
    ms.push(x)

ms.printStack()

print(ms.min())

print(f'Pop Element: {ms.pop()}')

ms.printStack()

print(ms.min())

print(f'Pop Element: {ms.pop()}')

ms.printStack()

print(ms.min())

print(f'Add Element 4: {ms.push(4)}')

ms.printStack()

print(ms.min())