import Queue
import abc
import threading

import Manager
import time

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
                # if there is data then send it to the listeners
                if raw_data is not None:
                    data = bytearray(raw_data)
                    print "byte0 ",  data[162]
                    self._incoming_messages.put(data)
                    self.publisher.publish(self._incoming_messages)  # publish the data


    @abc.abstractmethod
    def send(self, msg):
        pass

