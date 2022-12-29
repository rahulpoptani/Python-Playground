# Send Objects using Pipe. The object should be Piklable

from time import sleep
from random import random
from multiprocessing import Process, Pipe

class Animal:
    def __init__(self,name):
        self.name = name

obj = Animal('Dog')

def sender(connection, obj):
    print('Sender: Running', flush=True)
    connection.send(obj)
    sleep(1)
    connection.send(None)
    print('Sender: Done', flush=True)

def receiver(connection):
    print('Receiver: Running', flush=True)
    while True:
        item = connection.recv()
        if item is None:
            break
        else:
            print(f'Receiver got: {item.name}', flush=True)
    print('Receiver: Done', flush=True)

if __name__ == '__main__':
    conn1, conn2 = Pipe()
    sender_process = Process(target=sender, args=(conn2,obj))
    sender_process.start()
    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()
    sender_process.join()
    receiver_process.join()
