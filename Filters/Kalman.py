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
        self._A = A  # state trasition matrix
        self._B = B  # control matrix
        self._C = C  # measurement model
        self._Q = Q  # proccess noise covariance
        self._P = P  # predeciton
        self._R = R  ##measurement noise covariance
        self._state = x

    # move to the  next position
    def move(self, u, z):
        self.__predict(u)
        self.__update(z)

    # get the current state
    def getState(self):
        return self.state

    # predict the next state
    def __predict(self, u):
        self.state = self._A * self.state + self._B * u
        self.P = self._A * self._P * self._A.T + self._Q

    # update the model
    def __update(self, z):
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
