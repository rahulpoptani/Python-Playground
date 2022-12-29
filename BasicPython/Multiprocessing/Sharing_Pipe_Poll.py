
from time import sleep
from random import random
from multiprocessing import Process, Pipe

def sender(connection):
    print('Sender: Running', flush=True)
    # send data after 1 second
    sleep(1)
    connection.send('Some Value')
    print('Sender: Done', flush=True)

def receiver(connection):
    print('Receiver: Running', flush=True)
    # wait for 2 second and if data is available then process
    if connection.poll(timeout=2):
        item = connection.recv()
        print(f'Receiver got: {item}', flush=True)
    print('Receiver: Done', flush=True)

if __name__ == '__main__':
    conn1, conn2 = Pipe()
    sender_process = Process(target=sender, args=(conn2,))
    sender_process.start()
    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()
    sender_process.join()
    receiver_process.join()
