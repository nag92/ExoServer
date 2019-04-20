import Manager

import Sensors.RepeatedTimer
import Sensors.Sensor


class SensorManager(Manager.Manager):

    def __init__(self):
        """
        """

        self.sensors = {}

        self.types = {}
        # Tread to call the serial read at each time step
        # self.timer = Sensors.RepeatedTimer.RepeatedTimer(0.001, self.update)
        super(SensorManager, self).__init__()
        self.count = 0

    def get_sensors(self):
        """

        :return:
        :rtype: dict
        """
        return self.sensors

    def start(self):
        """
        start the tread to get data from the serial port
        :return:
        """
        self.timer.start()

    def stop(self):
        """
        start the tread to get data from the serial port
        :return:
        """

        self.timer.stop()

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

    def update(self, data):
        """
        Callback function for the timer,
        reads the serial port and parses the sensor packet into each sensor
        :return:
        """
        print len(data)
        self.count+=1
        # # put the raw packets in the sensors
        for key, sensor in self.sensors.iteritems():
            start, stop = sensor.byte_list
            packet = data[start - 1:stop]
            sensor.packet = packet


        # readings = self.parse(data)
        #
        # for key, items in self.types:
        #     for sensor_id in items:
        #         self.sensors[(type, sensor_id)] = readings[key][sensor_id]

        #self.publisher.publish(self.sensors)

    def parse(self, data):
        """
        Parse the sensor packet
        :param data: packet of the data
        :type data: array
        :return:
        """

        readings = {}
        next = 0

        while next < len(data) - 2:

            type = data[next]
            num_sensors = data[next + 1]
            start = next + 1
            length = Sensors.Sensor.Sensor.word_length[type]
            last_element = start + num_sensors * length + 1
            next = last_element
            mydata = data[start:last_element]

            readings[type] = []

            for index in xrange(start, last_element - 1, length):
                readings[type].append(data[index:(index + length)])

        return readings
