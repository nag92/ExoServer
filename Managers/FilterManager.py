from Managers import Manager

class FilterManager(Manager.Manager):

    def __init__(self):

        self._sensors = {}
        self._filters = {}
        super(FilterManager, self).__init__()

    def registar(self, filters, name):
        """
        Register a sensor with the manager. Each sensor is given an numeric ID.
        The IDs are created by the counting number of the occurance of the sensor type.
        :param sensor: Sensor.Sensor
        :return:
        """

        self._filters[name] = filters

    def get_sensor(self, name):
        return self._sensors[name]

    def get_sensors(self):
        return self._sensors

    def unregistar(self, key):
        # TODO write method to update the IDs
        del self._sensors[key]

    def update(self, sensors):
        """

        :type SM: dict
        """

        for key, sensor in sensors.iteritems():

            filters = self._filters[sensor.name]
            reading = sensor.raw_values
            sensor.filtered = True
            for filter in filters:
                reading = filter.update(reading)
            sensor.filtered_values = reading
