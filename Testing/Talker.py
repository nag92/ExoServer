# import binascii
# import socket
# import struct
# import sys
#
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('localhost', 1234)
# sock.bind(server_address)
# sock.listen(1)
#
# while True:
#     MESSAGE = b'\x09\x00\x09'
#     sock.send(MESSAGE)
#     print >> sys.stderr, '\nwaiting for a connection'
#     connection, client_address = sock.accept()
#     try:
#        pass
#
#     finally:
#         connection.close()
import socket
from struct import *
host = ''  # Symbolic name meaning all available interfaces
port = 12345  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print host, port
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:

    try:
        data = conn.recv(2048)

        if not data: break

        print "Client Says: " + data
        MESSAGE = pack('dd', -1, -1)

        conn.sendall(MESSAGE)

    except socket.error:
        print "Error Occured."
        break

conn.close()
