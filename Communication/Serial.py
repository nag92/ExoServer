import socket

from Managers import CommunicationManager
import serial
import time


class Serial(CommunicationManager.CommunicationManager):
    """
    implements the communucation class
    """

    def __init__(self, port="/dev/ACM0"):
        """

        :param host: name of host
        :param port: name of port
        """
        self.port = port
        self.conn = None
        super(Serial, self).__init__()

    def setup(self, baud=19200, port="/dev/ttyUSB0"):
        """
        set up the communication server
        :return:
        """
        self.port = port
        self._server = serial.Serial(port=port,
                                     baudrate=int(baud),
                                     parity=serial.PARITY_EVEN,
                                     bytesize=serial.EIGHTBITS)

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
        data = []

        if self._server.inWaiting() > 0:
            data = self._server.readline()
            return data


    def send(self, msg):
        """

        :param msg: data to be sent
        :return: None:q
        """
        self._server.write(msg)
