from Queue import Queue

# Create a Queue with initial elements from 1..10
q1 = Queue()
for x in range(1,11):
    q1.enqueue(x)

print('Current Queue')
q1.printQueue()
print('Reverse Queue at position 5')
q1.reverseK(5)
q1.printQueue()

