from random import random
from time import sleep
from multiprocessing import Process, Pipe

def task(connection):
    data = random()
    print(f'Generated {data}', flush=True)
    sleep(data)
    connection.send(data)

if __name__ == '__main__':
    conn1, conn2 = Pipe()
    process = Process(target=task, args=(conn2,))
    process.start()
    value = conn1.recv()
    print(f'Returned {value}')
