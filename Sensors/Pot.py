import Sensor


class Pot(Sensor.Sensor):

    def __init__(self, name,byte_list, side):
        super(Pot, self).__init__(name,byte_list, side)
        self._type = Sensor.Sensor.POT


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

    def get_angle(self):

        return self.filtered_values - self.offset

    def _raw_value_setter(self, blocks):
        values = 1 * [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values

