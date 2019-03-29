import abc

class Manager(object):

    def __init__(self):

        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

    @abc.abstractmethod
    def notify(self, observable, *args, **kwargs):
        pass

