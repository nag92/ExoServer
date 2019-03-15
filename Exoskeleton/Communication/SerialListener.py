import serial
import Queue
import threading
import datetime

class SerialListener():


    def __init__(self, port, baud):


        self.baud = baud
        self.port = port
        self.serial_port = serial.Serial(self.port, self.baud, timeout=0)
        self.connected = False
        self._data = Queue.queue()
        self.thread = threading.Thread(target=self.read())

    def start(self):
        self.thread.start()

    def connect(self):
        self.connected = True


    def disconnect(self):
        self.connected = False

    @property
    def data(self):
        return self._data


    @data.setter
    def data(self, data):
        self._data = data

    def read(self):

        while not self.connected:

            if self.serial_port.in_waiting > 0:
                self._data = self.serial_port.readline().decode()
