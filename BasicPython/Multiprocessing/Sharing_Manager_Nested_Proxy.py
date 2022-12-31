# Need for nested proxy:
    # We may use a manager to host a list and interact with the list from multiple processes via the proxies.
    # We may then add objects to the list, such as dicts.
    # This is a problem: the dict is not hosted by the manager and is only local to the process that created and added it to the list.
    # When another process attempts to modify the dict, it will not share a copy with the process that added it.
    # Instead, we must use nested proxy objects.

from multiprocessing import Process
from multiprocessing import Manager

def task(shared_list):
    item = shared_list[0]
    print(f'Task Before: {item}', flush=True)
    item['a'] = 1
    item['b'] = 1
    item['c'] = 1
    print(f'Task After: {item}', flush=True)

if __name__ == '__main__':
    with Manager() as manager:
        list_proxy = manager.list()
        dict_item = manager.dict({'a':0,'b':0,'c':0})
        list_proxy.append(dict_item)        
        print(f'Main Before: {list_proxy[0]}', flush=True)
        process = Process(target=task, args=(list_proxy,))
        process.start()
        process.join()
        print(f'Main After: {list_proxy[0]}', flush=True)
