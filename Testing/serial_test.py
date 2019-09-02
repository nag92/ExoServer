import time

from Managers import SerialManager

serial = SerialManager.SerialManager("/dev/ttyACM0", 9600)
serial.connect()
serial.start()

while 1:
    serial.write_data(45)
    if serial.have_data():
        print serial.get_data()