import os
import sys
import socket
import time

server_address = './uds_socket'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)


sock.send(b'hello world'*10000)
# time.sleep(10)
# sock.send(b'done')
sock.close()
