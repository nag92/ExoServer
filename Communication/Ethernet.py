import socket

from Managers import CommunicationManager


class Ethernet(CommunicationManager.CommunicationManager):

    def __init__(self, host, port):
        self._host = host
        self._port = port
        super(Ethernet, self).__init__()

    def setup(self):
        self.server(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        self.server.bind((self._host, self._port))
        self.server.setblocking(False)

    def start(self):
        super(Ethernet, self).start()

    @property
    def server(self):
        return super(Ethernet, self).server()

    def connect(self, SM):
        super(Ethernet, self).connect(SM)

    def disconnect(self):
        super(Ethernet, self).disconnect()

    def have_data(self):
        return super(Ethernet, self).have_data

    @property
    def get_data(self):
        return super(Ethernet, self).get_data()

    def read_port(self):
        return self.server.recv(1024)

    def send(self, msg):
        raise NotImplementedError
        pass

    def decode(self, msg):
        return msg
