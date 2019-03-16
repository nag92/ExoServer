import abc


class Sensor(object):


    ACCEl = 0
    GYRO = 1
    POT = 2
    FSR = 3
    CLIFF = 4

    word_length = []
    word_length[ACCEl] = 3
    word_length[GYRO] = 3
    word_length[POT] = 1
    word_length[FSR] = 1

    def __init__(self,  name):

        self._name = name
        self._type = None
        self._values = None
        self._offset = 0
        self._orientation = None
        self.word_length = 0
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def offset(self):
        return self._offset


    @offset.setter
    def offset(self, offset):
        self._offset = offset


    @property
    def orientation(self):
        return self._offset


    @orientation.setter
    @abc.abstractmethod
    def orientation(self, orientation):
        self.orientation = orientation


    @abc.abstractmethod
    def reset(self):
        pass


    @abc.abstractmethod
    def get_values(self):
        pass

    @abc.abstractmethod
    def set_values(self, values):
        self._values = values

