from threading import Thread
import copy
class Publisher:
    """
    Publisher class to handle the sending of messages
    """

    def __init__(self):
        """
        create a list of subsribers
        """
        self.subscribers = dict()

    def register(self, who, callback=None):
        """
        registar a subscriber and callback for the publisher
        :param who: Manager class to call
        :param callback: function to be called
        :return:
        """
        if callback == None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):
        """
        remove a subscriber
        :param who: manager to remove
        :return: None
        """
        del self.subscribers[who]

    def publish(self, message):
        """
        publish a message to the subscribers
        :param message:
        :return:
        """
        for subscriber, callback in self.subscribers.items():

            t = Thread(target=callback( message ))
            t.start()
            # callback(message)
