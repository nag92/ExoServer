import socket

from Managers import CommunicationManager
import serial

class Serial(CommunicationManager.CommunicationManager):
    """
    implements the communucation class
    """

    def __init__(self, port):
        """

        :param host: name of host
        :param port: name of port
        """
        self.port = [port]
        self.conn = None
        super(Serial, self).__init__()

    # def setup(self):
    #     """
    #     set up the communication server
    #     :return:
    #     """
    #
    #     self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self._server.connect((self.host, self.port))
    #     self._server.sendall(b'hello')  # need to send a message to start

    def setup(self, port="/dev/ACM0"):
        """
        set up the communication server
        :return:
        """
        self.port = port
        self._server = serial.Serial(self.port,
                                     baudrate=19200,
                                     parity=serial.PARITY_EVEN,
                                     bytesize=serial.EIGHTBITS)
        self._server.open()

    def start(self):
        """
        starts the communication
        :return:
        """
        super(Serial, self).start()

    def disconnect(self):
        """
        stop the communication
        :return:
        """
        super(Serial, self).disconnect()

    def have_data(self):
        """
        not used
        :return:
        """
        return super(Serial, self).have_data()

    @property
    def get_data(self):
        return super(Serial, self).get_data()

    def read_port(self):
        """
        read from the port
        :return:
        """
        # get the data
        data = self._server.readline()
        # check is data is avaible and the correct length, this has to be updated with the
        # correct check method

        if data and len(data) == 159:
            return data
        else:
            return None


    def send(self, msg):
        raise NotImplementedError
