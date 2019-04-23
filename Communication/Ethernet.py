import socket

from Managers import CommunicationManager


class Ethernet(CommunicationManager.CommunicationManager):
    """
    implements the communucation class
    """

    def __init__(self, host='', port=12345):
        """

        :param host: name of host
        :param port: name of port
        """
        self.host = host
        self.port = port
        self.conn = None
        super(Ethernet, self).__init__()

    def setup(self):
        """
        set up the communication server
        :return:
        """
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.connect((self.host, self.port))
        self._server.sendall(b'g')

    def start(self):
        super(Ethernet, self).start()


    def disconnect(self):
        super(Ethernet, self).disconnect()

    def have_data(self):
        return super(Ethernet, self).have_data

    @property
    def get_data(self):
        return super(Ethernet, self).get_data()

    def read_port(self):
        # self._server.sendall(b'q')
        data = self._server.recv(2048)
        if data and len(data) == 159:
            return data
        else:
            return None


    def send(self, msg):
        raise NotImplementedError
        pass

    def decode(self, msg):
        return msg
