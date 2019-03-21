


class Joint(object):

    def __init__(self, IMU, pot, FSR=None, cliff=None):
        self._IMU = IMU
        self._pot = pot
        self._FSR = FSR
        self._cliff = cliff

