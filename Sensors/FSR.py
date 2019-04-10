import Sensor


class FSR(Sensor.Sensor):

    def __init__(self, name):
        super(FSR, self).__init__(name)
        self._type = Sensor.Sensor.GYRO


    @property
    def offset(self):
        return super(FSR, self).offset()

    @property
    def orientation(self):
        return super(FSR, self).orientation()

    def reset(self):
        pass

    def _raw_value_setter(self, blocks):
        values = 1 * [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values





