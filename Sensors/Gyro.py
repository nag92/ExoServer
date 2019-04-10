import Sensor


class Gyro(Sensor.Sensor):

    def __init__(self, name):
        super(Gyro, self).__init__(name)
        self._type = Sensor.Sensor.GYRO


    @property
    def offset(self):
        return super(Gyro, self).offset()

    @property
    def orientation(self):
        return super(Gyro, self).orientation()

    def reset(self):
        pass

    def _raw_value_setter(self, blocks):
        values = 3 * [0]
        values[0] = self.parse(block1=blocks[4], block2=blocks[5])
        values[1] = self.parse(block1=blocks[2], block2=blocks[3])
        values[2] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values




