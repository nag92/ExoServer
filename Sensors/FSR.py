import Sensor


class FSR(Sensor.Sensor):

    def __init__(self, name, byte_list, side):
        super(FSR, self).__init__(name, byte_list, side)
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
        values = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values
