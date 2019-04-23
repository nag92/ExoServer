'''
Created on Jul 3, 2015

@author: nathaniel
generial linear Kalman fitler
'''
import numpy as np


# step

class Kalman:
    # take in all the parameters of the linear kalman filter
    def __init__(self, A, B, C, Q, P, R, x):
        """

        :param A: state trasition matrix
        :param B: control matrix
        :param C: measurement model
        :param Q: proccess noise covariance
        :param P: predeciton
        :param R: measurement noise covariance
        :param x: state vector
        :type A: numpy.matrix
        :type B: numpy.matrix
        :type C: numpy.matrix
        :type Q: numpy.matrix
        :type P: numpy.matrix
        :type R: numpy.matrix
        :type x: numpy.matrix
        """
        self._A = A
        self._B = B
        self._C = C
        self._Q = Q
        self._P = P
        self._R = R
        self._state = x

    def move(self, u, z):
        """
        move the system forward

        :param u: cmd to the system
        :param z: sensor update
        :type u: numpy.matrix
        :type z: numpy.matrix
        :return: None
        """

        self.__predict(u)
        self.__update(z)

    # get the current state
    def getState(self):
        """
        get the state of the system
        :return: state
        :type: numpy.matrix
        """
        return self.state


    def __predict(self, u):
        """
        predict the next state
        :param u: cmd for the system
        :type u: numpy.matrix
        :return: None
        """
        self.state = self._A * self.state + self._B * u
        self.P = self._A * self._P * self._A.T + self._Q

    def __update(self, z):
        """
        update the system
        :param z: sensor update
        :type z: numpy.matrix
        :return: None
        """
        # find the kalman gain
        K = self.P * (self._C.T) * np.linalg.inv((self._C * self.P * (self._C.T) + self._R))
        # get the current state
        self.state = self.state + K * (z - self._C * self.state)
        # get the next prediction
        size = self.state.shape[0]
        self.P = (np.eye(size) - K * self._C) * self.P

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value

    @property
    def B(self, value):
        return self._B

    @B.setter
    def B(self, value):
        self._B = value
