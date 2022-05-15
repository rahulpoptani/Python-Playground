from Stack import Stack


# Create a stack
s1 = Stack()
for _ in range(5):
    s1.push(_)
s1.printStack()
print(f'Peek of Stack: {s1.peek()}')