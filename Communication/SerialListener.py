import serial
import queue
import threading
import datetime
import struct
class SerialListener():


    def __init__(self, port, baud):


        self.baud = baud
        self.port = port
        self.serial_port = serial.Serial(self.port, self.baud, timeout=0)
        self.connected = False
        self._data = queue.Queue(maxsize=20)
        print "to"
        self.thread = threading.Thread(target=self.read)


    def start(self):
        self.thread.start()

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def have_data(self):
        return not self._data.empty()

    def get_data(self):
        return self.temp #self._data.get()

    def read(self):

        while not self.connected:

            if self.serial_port.in_waiting > 0:
                ts = datetime.datetime.now().timestamp()
                #vF, = struct.unpack('<f', data)
                self._data.put( ( ts, self.serial_port.readline().decode()))
