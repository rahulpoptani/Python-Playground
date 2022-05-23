from QueueList import QueueList

q1 = QueueList()
print('Adding Elements in Queue')
for x in range(1,11):
    q1.enqueue(x)

q1.printQueue()

print('Front: {}'.format(q1.front()))

print('Rear: {}'.format(q1.rear()))

print('Reverse Queue at position 5')
q1.reverseK(5)
q1.printQueue()

print('Dequeue: {}'.format(q1.dequeue()))
q1.printQueue()

print('Enqueue: {}'.format(q1.enqueue(11)))
q1.printQueue()
