ACCEl = 0
GYRO = 1
POT = 2
FSR = 3
CLIFF = 4

word_length = {}
word_length[ACCEl] = 3
word_length[GYRO] = 3
word_length[POT] = 1
word_length[FSR] = 1


def update(data):
    readings = self.parse(data)

    for key, items in self.types:
        for sensor_id in items:
            self.sensors[(type, sensor_id)] = readings[key][sensor_id]


def parse(data):
    readings = {}

    next = 0

    while next < len(data) - 2:

        type = data[next]
        num_sensors = data[next + 1]
        start = next + 1
        length = word_length[type]
        last_element = start + num_sensors * length + 1
        next = last_element
        mydata = data[start:last_element]
        print
        num_sensors

        print
        mydata

        readings[type] = []

        for index in xrange(start, last_element - 1, length):
            readings[type].append(data[index:(index + length)])


data = [0, 3, 5, 5, 5, 6, 6, 6, 7, 7, 7, 2, 3, 7, 8, 6]
parse(data)
