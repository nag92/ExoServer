import Queue
import abc
import threading

import Manager


class CommunicationManager(Manager.Manager):

    def __init__(self):


        self.thread = threading.Thread(target=self.read)
        self.connected = False
        # queue holding the data
        self._incoming_messages = Queue.Queue(maxsize=20)
        self._outgoing_messages = Queue.Queue(maxsize=20)
        # tread for reading the serial port
        self._server = None
        self.setup()
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
                raw_data = self.read_port()
                self.publisher.publish(bytearray(raw_data))  # publish the data

    @abc.abstractmethod
    def send(self, msg):
        pass

    @abc.abstractmethod
    def decode(self, msg):
        """
        Not using this
        :rtype: List[float]
        """
        if bin(int(msg[0], base=16)) == '0b11111111' and bin(int(msg[1], base=16)) == '0b0':

            raise Exception

        else:

            decoded_data = []  # type: List[float]
            for index in xrange(3, len(msg) - 1):
                decoded_data.append(msg[index:index + 2])

        return decoded_data
