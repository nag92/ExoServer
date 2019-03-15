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

    def __init__(self, id, pin):
        self._id = id
        self._pin = pin
        self._type = None
        self._values = None
        self._offset = 0
        self._orientation = None
        self.word_length = 0
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

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
    def orientation(self, orientation):
        self.orientation = orientation


    @abc.abstractmethod
    def reset(self):
        pass


    @abc.abstractmethod
    def get_values(self):
        pass

    @abc.abstractmethod
    def set_values(self):
        pass
