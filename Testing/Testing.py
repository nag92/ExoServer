import time

from Communication.SerialListener import SerialListener



serial = SerialListener("/dev/ttyS4", 9600)



for i in xrange(3):
    print serial.get_data()
    time.sleep(1)

serial.start()

for i in xrange(3):
    print serial.get_data()
    time.sleep(1)
