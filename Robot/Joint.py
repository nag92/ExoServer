class Joint(object):

    def __init__(self, IMU, pot, FSRs=None, cliff=None):
        self._IMU = IMU
        self._pot = pot
        self._FSRs = FSRs
        self._cliff = cliff

    @property
    def FSRs(self):
        return self._FSRs

    @FSRs.setter
    def FSRs(self, value):
        self._FSRs = value

    @property
    def IMU(self):
        return self._IMU

    @IMU.setter
    def IMU(self, value):
        self._IMU = value

    @property
    def pot(self):
        return self._pot

    @pot.setter
    def pot(self, value):
        self._pot = value

    @property
    def cliff(self):
        return self._cliff

    @cliff.setter
    def cliff(self, value):
        self._cliff = value
