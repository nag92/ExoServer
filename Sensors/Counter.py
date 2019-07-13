from lib.Exoskeleton.SensorBase import Sensor


class Counter(Sensor.Sensor):

    def __init__(self, name, byte_list, side):
        super(Counter, self).__init__(name, byte_list, side)
        self._type = Sensor.Sensor.POT

    @property
    def offset(self):
        return super(Counter, self).offset()

    @property
    def orientation(self):
        return super(Counter, self).orientation()

    def reset(self):
        pass

    def _raw_value_setter(self, blocks):
        values = 1 * [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values

    def parse(self, block1, block2,block3):
        pass
