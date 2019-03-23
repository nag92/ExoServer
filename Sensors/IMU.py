
import numpy as np
import math
from Filters import Kalman
from Sensors import Accel, Gyro, Mag


class IMU(object):

    def __init__(self, name, accel, gyro, mag):
        """

        :type accel: Accel
        :type gyro: Gyro
        :type mag: Mag

        """
        self._name = name
        self.accel = accel
        self.gyro = gyro
        self.mag = mag
        self._orentation = np.array([0, 0, 0])
        self._angular_velocity = np.array([0, 0, 0])


    def setup(self):
        pass#gx, gy, gz = 9.81*self._accel._orientation
        #H = np.matrix([  [  0, gz, -g  ]    ])

    @property
    def name(self):
        return self._name


    def get_accel_angles(self):

        x,y,z = self.accel.filtered_values()
        roll = math.atan2(y, z)
        pitch = math.atan2((- x), math.sqrt(y * y + z * z))
        return roll, pitch

    @property
    def orentation(self):
        return self._orentation

    @orentation.setter
    def orentation(self, orentation):
        self._orentation = orentation

    @property
    def angular_velocity(self):
        return self._orentation

    @angular_velocity.setter
    def angular_velocity(self, angular_velocity):
        self._angular_velocity = angular_velocity


    def update(self):
        pass
