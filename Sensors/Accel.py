import Sensor




class Accel(Sensor.Sensor):

    def __init__(self, name):
        super(Accel, self).__init__(name)
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



