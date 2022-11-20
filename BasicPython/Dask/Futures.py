import time

def inc(x):
    time.sleep(1)
    return x+1

inputs = [1,2,3,4,5,6,7,8,9,10]
results = []

start = time.perf_counter()

for x in inputs:
    result = inc(x)
    results.append(x)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')
print(inputs, results)