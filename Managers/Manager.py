import abc

from Observer import Publisher, Subscriber


class Manager(object):

    def __init__(self):
        self.publisher = Publisher.Publisher()
        self.subscriber = None

    def register_sub(self, manager):
        """

        :param manager: Manger to listen to the publisher
        :type manager: Manager.Manager
        :return:
        """
        self.publisher.register(manager, manager.generate_subscriber().callback)

    @abc.abstractmethod
    def update(self, data):
        """
        overide function to be called
        :param data: anything
        :return:
        """
        pass

    def generate_subscriber(self):
        """
        generate a subsciber for the Manager
        :return: Subscriber.Subscriber
        """
        self.subscriber = Subscriber.Subscriber(self.update)
        return self.subscriber
