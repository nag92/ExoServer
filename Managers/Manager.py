import abc
from Observer import Publisher

class Manager(object):

    def __init__(self):

        self.pub = None
        self.subs = {}


    def register_pub(self, pub):
        self.pub = pub

