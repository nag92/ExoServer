from lib.Exoskeleton.SensorBase import TempertureBase


class Temperature(TempertureBase.TemperatureBase):

    def __init__(self, name, byte_list, side):
        self.byte_list = byte_list
        super(Temperature, self).__init__(name, side)

    @property
    def offset(self):
        return super(Temperature, self).offset()

    @property
    def orientation(self):
        return super(Temperature, self).orientation()

    def reset(self):
        pass

    def get_angle(self):
        return self.get_values() - self.offset

    def _raw_value_setter(self, blocks):
        values = 1 * [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values

    def parse(self, block1, block2):
        data = super(Temperature, self).parse(block1, block2)
        return data
