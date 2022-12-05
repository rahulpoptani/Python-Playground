# Race condition is when two or more thread tries to change the state of the object parallely which leads to incosistent results
# this should be avoided using shared threading.Lock

import threading

# addition into global variable
def adder(amount, repeats, lock):
    global value
    for _ in range(repeats):
        with lock:
                value += amount

# substraction from global value
def subtractor(amount, repeats, lock):
    global value
    for _ in range(repeats):
        with lock:
            value -= amount

# define global value
value = 0
# define lock to protect the shared variable
lock = threading.Lock()

# start thread making additions
adder_thread = threading.Thread(target=adder, args=(100, 1000000, lock))
adder_thread.start()

# start thread making substractions
subtractor_thread = threading.Thread(target=subtractor, args=(100, 1000000, lock))
subtractor_thread.start()

# wait for both thread to finish
adder_thread.join()
subtractor_thread.join()

# print value from thread
print(f'Final Value: {value}')