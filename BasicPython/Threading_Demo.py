import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping')


# Both will take 1 second each sequentially - running synchronously
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()
# will result in Finish in 0 seconds and get output from both the methods
# the method will run concurrently but wont wait for both to complete
# 1. t1 will start
# 2. t1 will start
# 3. finish time calculation with 0 seconds
# 4. t1 complete
# 5. t2 complete 


# If we want to wait for the thread to finish before calculating the finish time, we have to join the method
t1.join()
t2.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')



#################################################################################################################

# Running the same method 10 times in loop to check the performance


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done Sleeping')

start = time.perf_counter()

thread_list = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    thread_list.append(t)

for thread in thread_list:
    thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

# Result: Normally will take 15 seconds but took only 1.5 second



#################################################################################################################


