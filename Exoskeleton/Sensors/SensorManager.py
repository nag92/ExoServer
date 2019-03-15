
import threading

class SensorManager(object):



    def __init__(self):
        self.sensors = {}
        pass


    def registar(self, sensor):
        self.sensors[sensor.id] = sensor

    def unregistar(self, key):
       del self.sensors[key]


    def
