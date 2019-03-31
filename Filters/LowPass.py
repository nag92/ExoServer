import numpy as np
import BaseFilter


class LowPass(BaseFilter.BaseFilter):

    def __init__(self, alpha):
        self._alpha = alpha
        self._y = 0
        super(LowPass, self).__init__()

    def update(self, value):

        self._y = self.y  + self._alpha * ( value - self._y)
        return self._y

