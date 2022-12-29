# In multiprocessing, a pipe is a connection between two processes in Python.
# A Queue is designed to be used with multiple producers and multiple consumers in mind, 
# whereas a Pipe is intended for a pair of processes only.

# The targeted and simpler nature of pipes can make them more efficient and potentially faster in sharing data between two processes.

from time import sleep
from random import random
from multiprocessing import Process, Pipe

def sender(connection):
    print('Sender: Running', flush=True)
    for i in range(10):
        value = random()
        sleep(value)
        connection.send(value)
    # all done. Send Sentinel value
    connection.send(None)
    print('Sender: Done', flush=True)

def receiver(connection):
    print('Receiver: Running', flush=True)
    while True:
        item = connection.recv()
        print(f'Receiver got: {item}', flush=True)
        if item is None:
            break
    print('Receiver: Done', flush=True)

if __name__ == '__main__':
    # By default, the first connection (conn1) can only be used to receive data, 
    # whereas the second connection (conn2) can only be used to send data.
    conn1, conn2 = Pipe()
    sender_process = Process(target=sender, args=(conn2,))
    sender_process.start()
    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()
    sender_process.join()
    receiver_process.join()
