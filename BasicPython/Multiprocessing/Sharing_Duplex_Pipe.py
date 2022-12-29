# A multiprocessing.Pipe can be used to both send and receive data between two processes.
# This is called a duplex or bidirectional pipe and can be achieved by setting the “duplex” argument to True when creating a pipe.

# The connection objects can be made duplex or bidirectional.
# This can be achieved by setting the “duplex” argument to the constructor to True.

from time import sleep
from random import random
from multiprocessing import Process, Pipe

def generate_send(connection, value):
    new_value = random()
    sleep(new_value)
    value = value + new_value
    print(f'Sending {value}', flush=True)
    connection.send(value)

def pingpong(connection, send_first):
    print('Process Running', flush=True)
    # check if this process should seed the process
    if send_first:
        generate_send(connection, 0)
    while True:
        value = connection.recv()
        print(f'Received {value}', flush=True)
        generate_send(connection, value)
        if value > 10:
            break
    print('Process Done', flush=True)

if __name__ == '__main__':
    conn1, conn2 = Pipe(duplex=True)
    player1 = Process(target=pingpong, args=(conn1,True))
    player2 = Process(target=pingpong, args=(conn2,False))
    player1.start()
    player2.start()
    player1.join()
    player2.join()