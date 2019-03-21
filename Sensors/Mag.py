import Sensor


class Mag(Sensor.Sensor):

    def __init__(self, name):
        super(Mag, self).__init__(name)
        self._type = Sensor.Sensor.Mag

    @property
    def name(self):
        return super(Mag, self).name()

    @property
    def type(self):
        return super(Mag, self).type()

    @property
    def offset(self):
        return super(Mag, self).offset()

    @property
    def orientation(self):
        return super(Mag, self).orientation()

    def reset(self):
        pass

    def set_values(self, values):
        super(Mag, self).set_values(values)
        # TODO other offset stuff



