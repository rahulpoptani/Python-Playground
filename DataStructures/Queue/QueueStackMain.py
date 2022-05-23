from QueueStack import QueueStack

qs = QueueStack()

qs.enqueue(1)

qs.printQueue()

qs.enqueue(2)
qs.enqueue(3)

qs.printQueue()

print('Dequeue: {}'.format(qs.dequeue()))

qs.printQueue()