import Sensor


class FSR(Sensor.Sensor):

    def __init__(self, name):
        super(FSR, self).__init__(name)
        self._type = Sensor.Sensor.GYRO

    @property
    def name(self):
        return super(FSR, self).name()



    @property
    def offset(self):
        return super(FSR, self).offset()

    @property
    def orientation(self):
        return super(FSR, self).orientation()

    def reset(self):
        pass

    def raw_values(self, values):
        super(FSR, self).raw_values(values)
        # TODO other offset stuff



