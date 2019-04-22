class Subscriber:
    def __init__(self, callback):
        """
        Calls to hold a callback function
        :param callback: function to be called
        :type callback: funct
        """
        self.callback = callback
