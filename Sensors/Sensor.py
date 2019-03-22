import abc


class Sensor(object):


    ACCEl = 0
    GYRO = 1
    MAG = 2
    POT = 3
    FSR = 4
    CLIFF = 5

    word_length = []
    word_length[ACCEl] = 3
    word_length[GYRO] = 3
    word_length[MAG] = 3
    word_length[POT] = 1
    word_length[FSR] = 1

    def __init__(self,  name):
        """
        This class handles a sensor.
        :param name: name of the sensor
        :type name: str
        """

        self._name = name
        self._type = None
        self._raw_values = 0
        self._filtred_values = 0
        self._offset = 0
        self._orientation = None
        self._error = 0
        pass

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
    def type(self):
        """

        :return:
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """

        :param type: type ID of the sensor
        :type type: int
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

    @property
    def filtered_values(self):
        """
        :return: values of the sensor
        """
        return self._raw_values

    @filtered_values.setter
    def filtered_values(self, values):
        """
        set the values for the sensor
        :param values: value of the sensor
        """
        self._raw_values = values
