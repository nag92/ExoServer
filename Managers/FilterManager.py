import Manager

class FilterManager(Manager.Manager):


    def __init__(self):

        self.sensors = {}

    def notify(self, observable, *args, **kwargs):
        self.update()


    def update(self):

        pass


