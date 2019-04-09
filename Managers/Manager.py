import abc
import Publisher

class Manager(object):

    def __init__(self):

        self.publisher = None

    def add_pub(self, pub):
        self.publisher = pub


