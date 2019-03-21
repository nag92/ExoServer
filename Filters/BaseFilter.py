import abc


class BaseFilter(object):

    def __init__(self):
        self.values = []

    @abc.abstractmethod
    def update(self, value):
        return value
