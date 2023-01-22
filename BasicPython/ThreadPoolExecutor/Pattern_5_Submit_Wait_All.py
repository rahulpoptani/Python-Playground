# submit all task and wait for all task to complete
# There are two approaches:
# 1. using wait(futures)
# 2. shutdown method or out of context manager
from time import sleep
from concurrent.futures import ThreadPoolExecutor, wait

def task(number):
    sleep(1)
    print(number)

with ThreadPoolExecutor(10) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    wait(futures)
print('All Done')

# Another approach will be to remove wait(futures)
# That way context manager will wait for all threads to complete and come out and print 'All Done'

with ThreadPoolExecutor(10) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
print('All Done')

# Another approach is to explicitly call shutdown

executor = ThreadPoolExecutor(10)
futures = [executor.submit(task, i) for i in range(10)]
executor.shutdown()
print('All Done')