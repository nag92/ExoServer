import Sensor


class Temp(Sensor.Sensor):

    def __init__(self, name):
        super(Temp, self).__init__(name)
        self._type = Sensor.Sensor.POT


    @property
    def offset(self):
        return super(Temp, self).offset()

    @property
    def orientation(self):
        return super(Temp, self).orientation()

    def reset(self):
        pass


    def get_angle(self):
        return self.get_values() - self.offset

    def _raw_value_setter(self, blocks):
        values = 1 * [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values

