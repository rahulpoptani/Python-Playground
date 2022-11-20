import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()

def do_something(second):
    print(f'Sleeping {second} second')
    time.sleep(second)
    print(f'Done Sleeping {second} second')




if __name__ == '__main__':
    
    # p1 = multiprocessing.Process(target=do_something, args=[1.5])
    # p2 = multiprocessing.Process(target=do_something, args=[1.5])
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    
    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     processes.append(p) 
    # for process in processes:
    #     process.join()
    
    # Using Concurrent Future Approach 
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     result = [executor.submit(do_something, sec) for sec in secs]
    #     for f in concurrent.futures.as_completed(result):
    #         print(f.result())
        
    # Using map approach
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # There will be no exception during the map phase
        results = executor.map(do_something, secs)
        # The exception will be raised when it's value is retrieved using the iterator. Handle inside for loop
        # Even if you don't retrieve, the content manager automatically joins all process and let them finish after context manager ends
        for result in results:
            print(result)
    
    
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')


