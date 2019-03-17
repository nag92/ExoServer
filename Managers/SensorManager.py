import Sensors.Sensor
import Sensors.RepeatedTimer
from Managers import SerialManager
import Manager

class SensorManager(Manager.Manager):

    def __init__(self, listener=SerialManager.SerialListener):
        """

        :param listener:
        :type listener: SerialListener.SerialListener
        """

        self.sensors = {}
        self.listener = listener
        self.types = {}
        # Tread to call the serial read at each time step
        #self.timer = Sensors.RepeatedTimer.RepeatedTimer(0.001, self.update)
        super(SensorManager, self).__init__()


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


    def registar(self, sensor=Sensors.Sensor.Sensor):
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
        #TODO write method to update the IDs
       del self.sensors[key]


    def registar_all_sensors(self, all_sensors):

        for sensor in all_sensors:
            self.registar(sensor)

    def notify(self, observable, *args, **kwargs):
        self.update()

    def update(self):
        """
        Callback function for the timer,
        reads the serial port and parses the sensor packet into each sensor
        :return:
        """

        if self.listener.have_data():

            data = self.listener.get_data()
            readings = self.parse(data)

            for key, items in self.types:
                for sensor_id in items:
                    self.sensors[(type, sensor_id)] = readings[key][sensor_id]
            self.notify_observers()


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

