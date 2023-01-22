# Exception raised from Task will atleast not break the Thread Pool, only the task will stop

from time import sleep
from concurrent.futures import ThreadPoolExecutor

# There are two ways to handle the exception:
# 1. Handle within task function
# 2. Handle when getting result

# Handle within task
def work():
    sleep(1)
    try:
        raise Exception('From task')
    except Exception:
        return 'Unable to get the result from task'
    return 'This wont execute'

with ThreadPoolExecutor() as executor:
    future = executor.submit(work)
    result = future.result()
    print(result)

# Handle while fetching result
def work():
    sleep(1)
    raise Exception('From task')
    return 'This wont execute'

with ThreadPoolExecutor() as executor:
    future = executor.submit(work)
    try:
        result = future.result()
    except Exception:
        print('Unable to get the result from task')

# Exception raised from submiting task using map cannot be handled