import Manager
import csv
import Sensors.Sensor
import Sensors.RepeatedTimer
from Managers import SerialManager
import Manager

class RecorderManager(Manager.Manager):

    def __init__(self, name, sensor_names):

        self._name = name + ".csv"
        with open(self._name, "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerpw(sensor_names)


    def update(self, SM):

        with open(self._name, "a") as f:
            writer = csv.writer(f, delimiter=",")
            for sensor in SM:
                writer.write(sensor.raw_values)

