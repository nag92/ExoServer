import csv

import Manager
import binascii

class LoggerManager(Manager.Manager):

    def __init__(self, name=None ):
        super(LoggerManager, self).__init__()
        self._recording = False

        if name is None:
            self._recording = False
        else:
            self.new_file(name)
            self.recording = True

    @property
    def recording(self):
        return self._recording

    @recording.setter
    def recording(self, value):
        self._recording = value

    def start_recording(self):
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


    def update(self, packet):
        """
        write values the the CSV file
        :type sensors: dict
        """

        if self.recording:

            data = packet

            with open(self._name, "a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(data)
