import abc
from Observer import Publisher, Subscriber

class Manager(object):

    def __init__(self):

        self.publisher = Publisher.Publisher()
        self.subscriber = None

    def register_pub(self, pub):
        self.pub = pub

    def update(self, data):
        pass

    def generate_subscriber(self):
        self.subscriber = Subscriber.Subscriber(self.update)
        return self.subscriber



