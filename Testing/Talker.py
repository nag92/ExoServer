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
import time
import struct

host = ''  # Symbolic name meaning all available interfaces
port = 12345  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print host, port
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

MESSAGE = ''
msg = struct.pack('B', 0)
MESSAGE += msg
MESSAGE += msg

for j in xrange(7):
    msg = struct.pack('B', 0)
    MESSAGE += msg
    MESSAGE += msg
    MESSAGE += msg

    for i in xrange(1, 9):
        msg = struct.pack('h', i)
        print msg
        MESSAGE = MESSAGE + msg

for j in xrange(3):
    msg = struct.pack('h', j)
    print msg
    MESSAGE = MESSAGE + msg

for j in xrange(3):
    msg = struct.pack('h', j)
    print msg
    MESSAGE = MESSAGE + msg

for j in xrange(3):
    msg = struct.pack('h', j)
    print msg
    MESSAGE = MESSAGE + msg

for j in xrange(3):
    msg = struct.pack('h', j)
    print msg
    MESSAGE = MESSAGE + msg

print MESSAGE
while True:

    try:
        data = conn.recv(2048)
        print "Client Says: " + data
        if not data:
            break
        else:

            # MESSAGE = bytearray([0x00, 0x00, 0x01, 0x01, 0x02, 0x02, ])
            # MESSAGE.append()
            while 1:
                conn.sendall(MESSAGE)
                print MESSAGE
                time.sleep(1)

                pass

    except socket.error:
        print "Error Occured."
        break

conn.close()
