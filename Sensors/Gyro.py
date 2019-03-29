import Sensor


class Gyro(Sensor.Sensor):

    def __init__(self, name):
        super(Gyro, self).__init__(name)
        self._type = Sensor.Sensor.GYRO


    @property
    def offset(self):
        return super(Gyro, self).offset()

    @property
    def orientation(self):
        return super(Gyro, self).orientation()

    def reset(self):
        pass

    def raw_values(self, values):
        super(Gyro, self).raw_values(values)
        # TODO other offset stuff



