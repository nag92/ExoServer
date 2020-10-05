
import os, pty
from serial import Serial
import threading


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
import struct
import time


MESSAGE = ''
msg = struct.pack('B', 1)
MESSAGE += msg
msg = struct.pack('B', 0)
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
    msg = struct.pack('h', j + 0.1)
    print msg
    MESSAGE = MESSAGE + msg

for j in xrange(3):
    msg = struct.pack('h', j + 0.1)
    print msg
    MESSAGE = MESSAGE + msg

for j in xrange(3):
    msg = struct.pack('h', j + 0.1)

    MESSAGE = MESSAGE + msg

for j in xrange(3):
    msg = struct.pack('h', j + 0.1)
    print msg
    MESSAGE = MESSAGE + msg

print "asldjf"
print MESSAGE

master, slave = pty.openpty() #open the pseudoterminal
s_name = os.ttyname(slave) #translate the slave fd to a filename

print s_name
while 1:
    # data = conn.recv(2048)
    os.write(master, MESSAGE+'\n')

    time.sleep(0.1)





