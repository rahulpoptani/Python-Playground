class Stack:
    def __init__(self):
        self.list = []
        self.ssize = 0
    
    # Time O(1)
    @property
    def isEmpty(self):
        return self.ssize == 0
    
    # Time O(1)
    def peek(self):
        if not self.isEmpty:
            return self.list[-1]
    
    # Time O(1)
    def size(self):
        return self.ssize
    
    # Time O(1)
    def push(self, value):
        self.ssize += 1
        self.list.append(value)
    
    # Time O(1)
    def pop(self):
        if self.isEmpty: return None
        self.ssize -= 1
        return self.list.pop()

    # Time O(n)
    def printStack(self):
        if self.size == 0: return None
        print('Stack: {}'.format(self.list))

    def __repr__(self):
        return str(self.list)
    
    # important method. Internally Used in Binary Tree traversal
    def __len__(self):
        return len(self.list)

    def __iter__(self):
        while len(self) > 0:
            yield self.pop()
