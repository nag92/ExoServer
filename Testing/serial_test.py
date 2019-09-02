import time

from Managers import SerialManager

serial = SerialManager.SerialManager("/dev/ttyACM2", 9600)
serial.connect()
serial.start()

while 1:
    if serial.have_data():
        print serial.get_data()