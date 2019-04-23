import csv

import Manager


class RecorderManager(Manager.Manager):

    def __init__(self, name, sensor_names):
        super(RecorderManager, self).__init__()
        self._name = name + ".csv"

        with open(self._name, "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(sensor_names)

    def update(self, sensors):
        """

        :type sensors: dict
        """
        with open(self._name, "a") as f:
            writer = csv.writer(f, delimiter=",")
            data = []
            for key, sensor in sensors.iteritems():
                data.append(sensor.get_values())
            writer.writerow(data)
