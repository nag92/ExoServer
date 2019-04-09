import Manager
from Sensors.Sensor import Sensor
from copy import deepcopy


class FilterManager(Manager.Manager):

    def __init__(self):

        self._sensors = {}
        self._filters = {}
        super(FilterManager, self).__init__()

    def registar(self, filters, sensor=Sensor):
        """
        Register a sensor with the manager. Each sensor is given an numeric ID.
        The IDs are created by the counting number of the occurance of the sensor type.
        :param sensor: Sensor.Sensor
        :return:
        """

        self._sensors[sensor.name] = sensor
        self._filters[sensor.name] = filters


    def get_sensor(self, name):
        return self._sensors[name]

    def get_sensors(self):
        return self._sensors

    def unregistar(self, key):
        # TODO write method to update the IDs
        del self._sensors[key]

    def update(self):

        for name, sensor in self._sensors.iteritems():  # type: (str, Sensor)

            filters = self._filters[name]
            reading = sensor.raw_values()

            for filter in filters:
                reading = filter.update(reading)

            sensor.filtered_values = reading
