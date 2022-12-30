from random import random
from time import sleep
from multiprocessing import Process, Value

def task(variable):
    data = random()
    print(f'Generated {data}', flush=True)
    sleep(data)
    variable.value = data

if __name__ == '__main__':
    variable = Value('f',0.0)
    process = Process(target=task, args=(variable,))
    process.start()
    process.join()
    print(f'Returned {variable.value}')
