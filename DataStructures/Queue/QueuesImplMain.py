from QueuesImpl import Queue
from QueuesImpl import Stack
from QueuesImpl import PriorityQueue
from QueuesImpl import PriorityQueueMax

fifo = Queue("1st","2nd")
fifo.enqueue("3rd")

print(len(fifo))
for element in fifo:
    print(element)
print(len(fifo))

########################################################################################################################

print("---- Stack ----")
lifo = Stack("1st","2nd","3rd")
print(len(lifo))
for element in lifo:
    print(element)
print(len(lifo))

########################################################################################################################

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# Radio station tuned in
print(messages.dequeue()) # Because Python heap is min heap the lowest priority is out, good for Dijkstra’s shortest path algorithm

# To Remove the highest priority item change the numbers to negative
messages = PriorityQueueMax()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# Brake pedal depressed
print(messages.dequeue()) # Highest priority removed

########################################################################################################################

# Corner Case. Items with same priority are removed based on value (string) comparison
# Case where the object is not comparable like custom class. In such case Python will give error. Introduce one more element to compare to avoid this issue. Ex: time of arrival