import abc
class Manager(abc):

    def __init__(self):

        self._observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

    @abc.abstractmethod
    def notify(self, observable, *args, **kwargs):
        pass

