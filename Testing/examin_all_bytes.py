import serial
import time
import binascii

def binbits(x, n):
    """Return binary representation of x with at least n bits"""
    bits = bin(x).split('b')[1]
    if len(bits) < n:
        ans = '0' * (n - len(bits)) + bits
    else:
        ans = bits

    return ans




if __name__ == '__main__':

    port = "/dev/ttyUSB0"
    baud = 19200
    server = serial.Serial(port=port,
                           baudrate=int(baud),
                           parity=serial.PARITY_EVEN,
                           bytesize=serial.EIGHTBITS)

    while 1:
        # only read if connected
            time.sleep(39 * 10 ** (-6))
            if server.inWaiting() > 0:
                raw_data = server.readline()
                if raw_data is not None:
                    if len(raw_data) > 162 and raw_data[0] == "X" and raw_data[1] == "O":
                        for ii, block in enumerate(raw_data):
                            print(str(ii+1) + ": " + str(binbits(int(binascii.hexlify(block), 16), 8) ))
