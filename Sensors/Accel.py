from lib.Exoskeleton.SensorBase import AccelBase
import binascii
from bitstring import BitArray

class Accel(AccelBase.AccelBase):

    def __init__(self, name, byte_list, side):
        super(Accel, self).__init__(name, side)
        self.byte_list = byte_list

    @property
    def offset(self):
        return super(Accel, self).offset()

    @property
    def orientation(self):
        return super(Accel, self).orientation()

    def reset(self):
        pass

    def _raw_value_setter(self, blocks):
        """
        Fills in the x,y,z components of the array
        :param blocks: byte array
        :return:
        """
        values = 3 * [0]
        values[0] = self.parse(block1=blocks[0], block2=blocks[1])
        values[1] = self.parse(block1=blocks[2], block2=blocks[3])
        values[2] = self.parse(block1=blocks[4], block2=blocks[5])
        self.raw_values = values

    def parse(self, block1, block2):
        """
        convers the bytes to a decimal value

        :param block1: byte 1
        :param block2: byte 2
        :type block1: byte
        :type block2: byte
        :return:
        """
        a = self.binbits(int(binascii.hexlify(block1), 16), 8)
        b = self.binbits(int(binascii.hexlify(block2), 16), 8)
        c = BitArray(bin=a + b)
        return c.int
