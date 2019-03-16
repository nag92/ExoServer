import Sensor




class Accel(Sensor.Sensor):

    def __init__(self, name):
        super(Accel, self).__init__(name)
        self._type = Sensor.Sensor.ACCEl

    @property
    def name(self):
        return super(Accel, self).name()

    @property
    def type(self):
        return super(Accel, self).type()

    @property
    def offset(self):
        return super(Accel, self).offset()

    @property
    def orientation(self):
        return super(Accel, self).orientation()

    def reset(self):
        pass

    def set_values(self, values):
        super(Accel, self).set_values(values)
        #TODO other offset stuff



