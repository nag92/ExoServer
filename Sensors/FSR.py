import Sensor


class FSR(Sensor.Sensor):

    def __init__(self, name, byte_list, side, ):
        super(FSR, self).__init__(name, byte_list, side)
        self._type = Sensor.Sensor.FSR

    @property
    def offset(self):
        return super(FSR, self).offset()

    def reset(self):
        pass

    def _raw_value_setter(self, blocks):
        """
        Fills in the components of the array
        :param blocks: byte array
        :return:
        """
        values = [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        self.raw_values = values
