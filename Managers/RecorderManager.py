import csv

import Manager


class RecorderManager(Manager.Manager):

    def __init__(self, sensor_names, name=None):
        super(RecorderManager, self).__init__()

        self._recording = False  #
        self.sensor_names = sensor_names
        if name is None:
            self._recording = False
        else:
            self.new_file(name)
            self.recording = True

    @property
    def _recording(self):
        return self._recording

    @_recording.setter
    def _recording(self, value):
        self._recording = value

    def stat_recording(self):
        """
        Start recording
        :return:
        """
        self.recording = True

    def stop_recording(self):
        """
        stop recording
        :return: None
        """
        self.recording = False

    def new_file(self, name):
        """
        Create a new file to record the sensor data too
        :param name:
        :return:
        """
        if self.recording:
            """
            Throw an error if in the middle of recording 
            """
            RuntimeError("IN THE MIDDLE OF RECORDING")
            return

        self._name = name + ".csv"
        with open(self._name, "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(self.sensor_names)

    def update(self, sensors):
        """
        write values the the CSV file
        :type sensors: dict
        """
        if self.recording:
            with open(self._name, "a") as f:
                writer = csv.writer(f, delimiter=",")
                data = []
                for key, sensor in sensors.iteritems():
                    data.append(sensor.get_values())
                writer.writerow(data)
