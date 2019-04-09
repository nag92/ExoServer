import Manager
from Observer import Subscriber
import csv
import Sensors.Sensor
import Sensors.RepeatedTimer
from Managers import SerialManager
import Manager

class RecorderManager(Manager.Manager):

    def __init__(self, name, sensor_names):

        super(RecorderManager,self).__init__()
        self._name = name + ".csv"

        with open(self._name, "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerpw(sensor_names)


    def update(self, sensors):
        """

        :type sensors: dict
        """
        with open(self._name, "a") as f:
            writer = csv.writer(f, delimiter=",")
            for key, sensor in sensors.iteritems():
                writer.write(sensor.values())





