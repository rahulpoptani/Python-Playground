'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''

from Common.Tags import STACK, QUEUE, DESIGN

class MyQueue:
    def __init__(self):
        self.inbox = []   # Stack for push operations
        self.outbox = []  # Stack for pop/peek operations

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def pop(self) -> int:
        self._shift()
        return self.outbox.pop()

    def peek(self) -> int:
        self._shift()
        return self.outbox[-1]

    def empty(self) -> bool:
        return not self.inbox and not self.outbox

    def _shift(self) -> None:
        """Pour inbox → outbox only when outbox is empty."""
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
# test case
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.pop())
obj.push(3)
print(obj.peek())
print(obj.empty())

'''
Operation   Time            Notes
-----------------------------------------------------------------------
push        O(1)            Always appends to inbox
pop         Amortized O(1)  Each element is shifted exactly once
peek        Amortized O(1)  Same as pop — shift only when needed
empty       O(1)            Checks both stacks
Space       O(n)            All n elements split across two stacks
'''