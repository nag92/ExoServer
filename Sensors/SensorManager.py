import Sensor
import RepeatedTimer

class SensorManager(object):



    def __init__(self, listener):
        self.sensors = {}
        self.listener = listener
        self.types = {}
        self.timer = RepeatedTimer.RepeatedTimer(0.01, self.update)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def registar(self, sensor):

        if sensor.type in self.types:
            id = len(self.types[sensor.type])
        else:
            id = 0
            self.types[sensor.type] = []

        self.types[sensor.type].append(id)
        self.sensors[(sensor.type, id)] = sensor


    def unregistar(self, key):
        #TODO write method to update the IDs
       del self.sensors[key]


    def update(self):

        if self.listener.have_data():

            data = self.listener.get_data()
            readings = self.parse(data)

            for key, items in self.types:
                for sensor_id in items:
                    self.sensors[(type, sensor_id)] = readings[key][sensor_id]


    def parse(self, data):

        readings = {}

        next = 0

        while next < len(data)-2:

            type = data[next]
            num_sensors = data[next+1]
            start = data[next + 2]
            length = Sensor.Sensor.word_length[type]
            last_element = start + num_sensors*length
            next = start + 1
            mydata = data[start:last_element]

            readings[type] = []

            for index in xrange(len(mydata)/num_sensors):
                first = index*length + 1
                last = index*length + 1 + 3
                readings[type].append([mydata[first:last]])














