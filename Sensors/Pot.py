import Sensor


class Pot(Sensor.Sensor):

    def __init__(self, name, byte_list, side):
        super(Pot, self).__init__(name, byte_list, side)
        self._type = Sensor.Sensor.POT

    @property
    def offset(self):
        return super(Pot, self).offset()

    @property
    def orientation(self):
        return super(Pot, self).orientation()

    def reset(self):
        pass

    def get_angle(self):
        return self.filtered_values - self.offset

    def _raw_value_setter(self, blocks):
        """
        Fills in the components of the array
        :param blocks: byte array
        :return:
        """
        values = [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values

    def parse(self, block1, block2):
        data = super(Pot, self).parse(block1, block2)
        return data
