
import serial
import binascii
from bitarray import bitarray




def binbits(x, n):
    """Return binary representation of x with at least n bits"""
    bits = bin(x).split('b')[1]
    if len(bits) < n:
        ans =  '0' * (n - len(bits)) + bits
    else:
        ans =  bits

    return ans

ser = serial.Serial(port="/dev/ttyUSB0",
                    baudrate=19200,
                    parity=serial.PARITY_EVEN,
                    bytesize=serial.EIGHTBITS)



while 1:

    line = ser.readline()
    if len(line) > 160:
        # print line[147]
        # print line[148]
        a = binbits(int(binascii.hexlify(line[147]), 16),8)
        b = binbits(int(binascii.hexlify(line[148]), 16),8)
        c = '0b' + a[0:4] + b
        print int(c,2)