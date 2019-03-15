import abc


class Sensor(object):

    ACCEl = "ACCEL"
    GYRO = "GYRO"
    POT = "POT"
    FSR = "FSR"
    CLIFF = "CLIFF"


    def __init__(self, id, pin):
        self._id = id
        self._pin = pin
        self._type = None
        self._values = None
        self._offset = 0
        self._orientation = None
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
