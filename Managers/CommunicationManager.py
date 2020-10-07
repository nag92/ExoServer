import Queue
import abc
import threading

import Manager
import time
import binascii

class CommunicationManager(Manager.Manager):

    def __init__(self):

        self.thread = threading.Thread(target=self.read)
        self.connected = False
        # queue holding the data
        self._incoming_messages = Queue.Queue(maxsize=20)
        self._outgoing_messages = Queue.Queue(maxsize=20)
        # tread for reading the serial port
        self._server = None

        super(CommunicationManager, self).__init__()

    @abc.abstractmethod
    def setup(self):
        pass

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        self._server = value

    def start(self):
        """
        Starts the tread to read from the sensor.
        :return:
        """
        self.connect()
        self.thread.start()

    def stop(self):
        """
        Starts the tread to read from the sensor.
        :return:
        """
        self.disconnect()

    def connect(self):
        """
        Connect to the device.
        :return:
        """
        self.connected = True

    def disconnect(self):
        """
        Diconnect to the device.
        :return:
        """
        self.connected = False

    @property
    def have_data(self):
        """
        Check if there is data in the queue.
        :return:
        :rtype bool
        """
        return not self._incoming_messages.empty()

    @abc.abstractmethod
    def read_port(self):
        pass

    def get_data(self):
        # type: () -> Queue.Queue
        """
        Get reading from the queue.
        :return:
        :rtype array
        """
        return self._incoming_messages

    def read(self):
        """
        continually read the server
        :return:
        """

        while 1:
            # only read if connected
            if self.connected:
                time.sleep(39 * 10 ** (-6))
                raw_data = self.read_port()

                if raw_data is not None:
                    #if len(raw_data) > 162 and raw_data[0] == "X" and raw_data[1] == "O":
                    #self._incoming_messages.put(raw_data)
                    self.publisher.publish(raw_data)  # publish the data
                    #print self.parse(raw_data[153], raw_data[154])


    @abc.abstractmethod
    def send(self, msg):
        pass

    ### REMOVE  AFTER TESTING
    def parse(self, block1, block2):
        """
        convers the bytes to a decimal value

        :param block1: byte 1
        :param block2: byte 2
        :type block1: byte
        :type block2: byte
        :return:
        """

        a = self.binbits(int(binascii.hexlify(block1), 16), 8)
        b = self.binbits(int(binascii.hexlify(block2), 16), 8)
        c = 3.3*int('0b' + a[0:4] + b, 2) / 4095

        return c

    def binbits(self, x, n):
        """Return binary representation of x with at least n bits"""
        bits = bin(x).split('b')[1]
        if len(bits) < n:
            ans = '0' * (n - len(bits)) + bits
        else:
            ans = bits

        return ans
