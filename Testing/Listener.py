import binascii
import socket
import struct
import sys
from struct import *

host = socket.gethostname()
port = 12345  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'Hello, world')
data = s.recv(2048)
s.close()
thing = bytearray(data)
print len(thing)
print int(thing[0] | thing[1] << 8)

# from struct import *

# a = pack('hhl', 1,2,3)
