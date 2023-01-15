import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1',8000)
server_socket.bind(server_address)
server_socket.setblocking(False)
server_socket.listen()
# register the socket for getting notifications with type of event interested in
selector.register(server_socket, selectors.EVENT_READ)

while True:
    # list of sockets that are ready for processing, along with event that triggered it
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1) # selector will timeout after 1 second

    if len(events) == 0:
        print('No events, waiting a bit more')
    
    for event, _ in events:
        # get the socket for the event
        event_socket = event.fileobj

        # if the event socket is same as server socket, this is connection attempt
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'I got a connection from {address}')
            # register the client that connected with our selector
            selector.register(connection, selectors.EVENT_READ)
        else:
            # if event socket is not server socket then receive data from the client and echo back
            data = event_socket.recv(1024)
            print(f'I got some data: {data}')
            event_socket.send(data)

# Open Powershell, type 'telnet localhost 8000'