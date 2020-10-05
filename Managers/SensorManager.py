import Manager
from collections import OrderedDict

class SensorManager(Manager.Manager):

    def __init__(self):
        """
        """

        self.sensors = OrderedDict()

        self.types = OrderedDict()
        # Tread to call the serial read at each time step
        # self.timer = Sensors.RepeatedTimer.RepeatedTimer(0.001, self.update)
        super(SensorManager, self).__init__()

    def get_sensors(self):
        """

        :return:
        :rtype: dict
        """
        return self.sensors

    def calibrate(self):

        for sensor in self.sensors:
            sensor.offset = sum(sensor.queue) / len(sensor.queue)

    def registar(self, sensor):
        """
        Regiestar a sensor with the manager. Each sensor is given an numeric ID.
        The IDs are created by the counting number of the occurance of the sensor type.
        :param sensor: Sensor.Sensor
        :return:
        """
        if sensor.type in self.types:
            id = len(self.types[sensor.type])
        else:
            id = 0
            self.types[sensor.type] = []

        self.types[sensor.type].append(id)
        self.sensors[(sensor.type, id)] = sensor

    def unregistar(self, key):
        # TODO write method to update the IDs
        del self.sensors[key]

    def registar_all_sensors(self, all_sensors):
        """
        Registar all the sensors
        :param all_sensors: a list of sensors
        :return:
        """

        for sensor in all_sensors:

            self.registar(sensor)

    def update(self, packet):
        """
        Callback function for the timer,
        reads the serial port and parses the sensor packet into each sensor
        :return:
        """
        data = packet.get()
        print("sensors")

        # # put the raw packets in the sensors
        for key, sensor in self.sensors.iteritems():
            start, stop = sensor.byte_list
            packet = data[start - 1:stop]
            sensor.packet = packet
            print(packet)
        self.publisher.publish(self.sensors)

    def get_sensor_names(self):
        names = []

        for name, sensor in self.get_sensors().iteritems():
            names.append(sensor.name)
        return names
