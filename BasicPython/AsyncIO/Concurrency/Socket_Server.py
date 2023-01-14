import socket

# socket.socket takes two parameters.
    # 1st = What type of address our socket will be able to interact with. In this case its hostname and port
    # 2nd = socket.SOCK_STREAM, means we use TCP protocol for communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SO_REUSEADDR = 1, allow use to reuse the port number after we stop and restart the application. Otherwise OS will take take time unbind the port
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1',8000)
server_socket.bind(server_address)
# listen for connection from clients who want to connect to server.
server_socket.listen()

try:
    # wait for the connection by calling accept. Blocking Call
    connection, client_address = server_socket.accept()
    print(f'I got a connection from: {client_address}')

    buffer = b''

    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f'I got data: {data}')
            buffer += data
    
    print(f'All the data is: {buffer}')
    # send data back to client
    connection.sendall(buffer)
finally:
    server_socket.close()

# Open Powershell, type 'telnet localhost 8000'