import concurrent.futures
import time

# Threads are used when the process is IO bound and not CPU bound (doing lot of processing)
# For CPU bound work do MultiProcessing instead 


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done Sleeping {seconds}'


# submit method schedule method to be executed and returns future object
# future object encapsulate execution of our function allows us to check in after its schedule. Running, Done, Result, etc.

# First Approach
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
    
#     print(f1.result())
#     print(f2.result())
    # Both will start at same time and return execution time as 1 second


# Second Approach
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(do_something, 1) for _ in range(10)]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
    # Result: All 10 completed in 1 second
     
# Changing Seconds
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something, sec) for sec in secs]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#     # Result: All 5 method starts together and completed one-by-one each second with total 5 seconds

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds')


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # using map method. Here you will get all the result at once after 5 seconds are over
    executor.map(do_something, secs)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

