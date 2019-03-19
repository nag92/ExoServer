import abc
import Queue
import threading
import Manager


class CommunicationManager(Manager.Manager):

    def __init__(self, ):
        self.setup()
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
        self.thread.start()

    def connect(self, SM):
        """
        Connect to the device.
        :return:
        """
        self.register_observer(SM)
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
        while not self.connected:
            raw_data = self.read_port
            data = self.decode(raw_data)
            self._incoming_messages.put(data)
            self.notify_observers(self.get_data)

    @abc.abstractmethod
    def send(self, msg):
        pass

    @abc.abstractmethod
    def decode(self, msg):
        pass
