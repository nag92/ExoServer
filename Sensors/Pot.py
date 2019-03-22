import Sensor


class Pot(Sensor.Sensor):

    def __init__(self, name):
        super(Pot, self).__init__(name)
        self._type = Sensor.Sensor.POT

    @property
    def name(self):
        return super(Pot, self).name()

    @property
    def type(self):
        return super(Pot, self).type()

    @property
    def offset(self):
        return super(Pot, self).offset()

    @property
    def orientation(self):
        return super(Pot, self).orientation()

    def reset(self):
        pass

    def raw_values(self, values):
        super(Pot, self).raw_values(values)
        # TODO other offset stuff



