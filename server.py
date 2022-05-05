import os
import socket

server_address = './uds_socket'

# Remove previous connections
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(1)
while True:
    # Each iteration is one connection
    try:
        clientsocket, address = server.accept()
        datas = []
        data = clientsocket.recv(1024)
        # Get all the data in the connection
        while data:
            datas.append(data)
            data = clientsocket.recv(1024) 
        # Join all the data together and print it
        print(''.join(map(lambda x: x.decode('utf-8'), datas)))
        clientsocket.close()
        print("Waiting for new connection")
    except KeyboardInterrupt:
        server.close()
        break
