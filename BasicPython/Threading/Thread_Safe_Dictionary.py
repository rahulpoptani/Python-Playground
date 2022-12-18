# Share dictionary data structure between threads

# Most dictionary operations are atomic, meaning they are thread safe
# Operations such as adding, removing, and reading a value on a dict are atomic.
# Specifically:
    # Adding a key and value mapping.
    # Replacing a value for a key.
    # Adding a dict to a dict via update().
    # Getting a list of keys via keys().
# This is only true at the time of writing because of a few specific considerations, such as:
    # The precise details on how these dict operations are converted to python virtual machine bytecode.
    # The use of the reference python interpreter.
    # The use of a Global Interpreter Lock (GIL) within the reference python interpreter.
# This means that depending on the thread-safety of these operations could be fragile in future versions of Python or when executing your Python program with alternate Python interpreters.

# Race conditions using dictionary
# A main source of race conditions when working with a dict is in performing operations that involve two or more steps.
# Example:
    # Thread A: Get a key from dict.
    # Thread A: Use key on dict.
# A context switch is possible between these two operations, allowing another thread to remove the entry from the dict in between.
# For example:
    # Thread A: Get a key from dict.
    # <context switch>
    # Thread B: Get same key from dict.
    # Thread B: Remove key from dict.
    # <context switch>
    # Thread A: Use key on dict.

# The right approach is used threading.Lock when removing items

from threading import Thread, Lock

def remove_items(shared_dict, lock, limit=1000):
    counter = 0
    # Once the lock is acquired, the thread can check if the key exists and then remove it, otherwise skip the key.
    with lock:
        for key in list(shared_dict.keys()):
            # Key exists check allow other threads to run while threads are context switched by the operating system 
            # as the lock is only held by a thread for a brief period
            if key in shared_dict:
                shared_dict.pop(key)
                counter += 1
                if counter > limit:
                    break

lock = Lock()
shared_dict = {i:i for i in range(1000000)}
print(f'Dict has {len(shared_dict)} items')
threads = [Thread(target=remove_items, args=(shared_dict, lock)) for _ in range(1000)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f'Dict has {len(shared_dict)} items')
