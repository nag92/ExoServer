import Queue
import abc


class Sensor(object):
    ACCEl = "ACCEl"
    GYRO = "GYRO"
    MAG = "MAG"
    POT = "POT"
    FSR = "FSR"
    CLIFF = "CLIFF"

    def __init__(self, name, byte_list, side, size=10):
        """
        This class handles a sensor.
        :param name: name of the sensor
        :type name: str
        """
        self.queue = Queue.Queue(maxsize=size)
        self._name = name
        self._type = None
        self._raw_values = None
        self._filtred_values = 0
        self._time = 0
        self._offset = 0
        self._orientation = None
        self._error = 0
        self._filtered_values = None
        self._filtered = False
        self._byte_list = byte_list
        self._packet = 0
        self._packet_order = None
        self._order = None
        self._side = side

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """
        set the name of the sensor

        :param name: name of sensor
        :type name: str
        """

        self._name = name

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        """
        set the name of the sensor

        :param name: name of sensor
        :type name: str
        """

        self._side = side

    @property
    def type(self):
        """

        :return:
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """

        :param type: type ID of the sensor
        :type type: str
        :return:
        """
        self._type = type

    @property
    def offset(self):
        """

        :return:
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        An offset to apply to the sensor
        :param offset:
        :return:
        """
        self._offset = offset

    @property
    def orientation(self):
        """

        :return: oren
        """
        return self._orientation

    @orientation.setter
    @abc.abstractmethod
    def orientation(self, orientation):
        """
        set the orentation of the sensor
        :param orientation:
        :return:
        """
        self.orientation = orientation

    @abc.abstractmethod
    def reset(self):
        pass

    @property
    def raw_values(self):
        """
        :return: values of the sensor
        """
        return self._raw_values

    @raw_values.setter
    def raw_values(self, values):
        """
        set the values for the sensor
        :param values: value of the sensor
        """
        self._raw_values = values

    @abc.abstractmethod
    def _raw_value_setter(self, value):
        pass

    @property
    def filtered_values(self):
        """
        :return: values of the sensor
        """

        return self._filtered_values

    @filtered_values.setter
    def filtered_values(self, values):
        """
        set the values for the sensor
        :param values: value of the sensor
        """
        self._filtered_values = values

    @property
    def time(self):
        """
        :return: values of the sensor
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        set the values for the sensor
        :param values: value of the sensor
        """
        self._time = time

    @property
    def filtered(self):
        """
        :return: values of the sensor
        """
        return self._filtered

    @filtered.setter
    def filtered(self, value):
        """
        set the values for the sensor
        :param values: value of the sensor
        """
        self._filtered = value

    def get_values(self):
        """
        Get the values of the sensor, it returns the filtered value only
        if the sensor is being filtered, else it returns the raw value
        :return:
        """
        if self._filtered:
            return self._filtered_values
        else:
            return self.raw_values

    @property
    def byte_list(self):
        return self._byte_list

    @property
    def packet(self):
        return self.queue.get()

    @packet.setter
    def packet(self, packet):
        """
        takes in the raw packet and converts it into a decmial
        and stores its
        :param packet:
        :return:
        """
        self._packet = packet
        self._raw_value_setter(packet)

    @abc.abstractmethod
    def parse(self, block1, block2):
        """
        convers the bytes to a decimal value

        :param block1: byte 1
        :param block2: byte 2
        :type block1: byte
        :type block2: byte
        :return:
        """
        return block1 | block2 << 8
