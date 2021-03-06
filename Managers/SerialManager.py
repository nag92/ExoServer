import datetime
import threading

import Manager
import Queue
import serial

"""
OLD DO NOT USE
"""
class SerialManager(Manager.Manager):

    def __init__(self, port="/dev/tty/AMC0", baud=9600):
        """
        Handles the serial communication with a device and decodes the serial stream

        :param port: name of the port
        :type port: str
        :param baud: baud rate
        :type baud: int
        """

        self.baud = baud
        self.port = port
        self.serial_port = serial.Serial(self.port, self.baud, timeout=0)
        self.connected = False

        # queue holding the data
        self._data = Queue.Queue(maxsize=20)

        # tread for reading the serial port
        self.thread = threading.Thread(target=self.read)

        super(SerialManager, self).__init__()

    def start(self):
        """
        Starts the tread to read from the sensor.
        :return:
        """
        self.thread.start()

    def connect(self):
        """
        Connect to the device.
        :return:
        """
        #self.register_observer(SM)
        self.connected = True

    def disconnect(self):
        """
        Diconnect to the device.
        :return:
        """
        self.connected = False

    def have_data(self):
        """
        Check if there is data in the queue.
        :return:
        :rtype bool
        """
        return not self._data.empty()

    def get_data(self):
        """
        Get reading from the queue.
        :return:
        :rtype array
        """
        return self._data.get()

    def write_data(self, data):
        """

        :param data: data to be written
        :return:
        """
        self.serial_port.write(data)

    def read(self):
        """
        Continuely read from the serial port and stores the reading
        in queue.
        :return:
        """

        while self.connected:

            if self.serial_port.inWaiting() > 0:
                # store the data in the queue
                self._data.put(self.serial_port.readline())
                #self.notify_observers()
