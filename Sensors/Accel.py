import Sensor


class Accel(Sensor.Sensor):

    def __init__(self, name, byte_list, side):
        super(Accel, self).__init__(name, byte_list, side)
        self._type = Sensor.Sensor.ACCEl

    @property
    def offset(self):
        return super(Accel, self).offset()

    @property
    def orientation(self):
        return super(Accel, self).orientation()

    def reset(self):
        pass

    @property
    def filtered_values(self):
        return super(Accel, self).filtered_values()

    def _raw_value_setter(self, blocks):
        """
        Fills in the x,y,z components of the array
        :param blocks: byte array
        :return:
        """
        values = 3 * [0]
        values[0] = self.parse(block1=blocks[4], block2=blocks[5])
        values[1] = self.parse(block1=blocks[2], block2=blocks[3])
        values[2] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values
