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
        data = None
        time.sleep(46 / 1000000.0)
        if self._server.inWaiting() >  0:
            data = self._server.readline()
        # check is data is avaible and the correct length, this has to be updated with the
        # correct check method

        if data and len(data) == 162 or data and len(data) == 159:
            return data
        else:
            return None


    def send(self, msg):
        """

        :param msg: data to be sent
        :return: None:q
        """
        self._server.write(msg)
