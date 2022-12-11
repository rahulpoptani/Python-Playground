# A race condition based on timing can be fixed by allowing the notify thread 
# to wait for the waiting thread to be ready before doing its work and calling notify().


from time import sleep
from threading import Thread, Condition, Event

# thread waiting to ve notified
# 3. The new thread wakes up, acquires the condition, sets the event and then waits on the condition.
def task(condition, event):
    # insert a delay
    sleep(0.5)
    # wait to be notified
    with condition:
        # indicate we are ready to be notified
        print('Thread Ready')
        event.set()
        print('Thread ready to be notified...')
        condition.wait()
    print('Thread Notified')

# create shared condition
condition = Condition()
# create share event
event = Event()
# create new thread
# 1. The new thread is then created and started, which immediately blocks for a moment.
Thread(target=task, args=(condition, event)).start()
# busy waiting for the new thread to be ready
print('Main: waiting for threads to get ready...')
# 2. the main thread enters its busy wait loop and checks the event ten times per second.
while not event.is_set():
    sleep(0.1)
print('Main: Notifying the thread')
# 4. The main thread notices that the event has been set, then acquires the condition and notifies the new thread.
with condition:
    condition.notify()
print('Main Done')


