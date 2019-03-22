import numpy as np
import BaseFilter


class LowPass(BaseFilter.BaseFilter):

    def __init__(self, alpha):
        self._alpha = alpha
        self._last = None
        super(LowPass, self).__init__()

    def update(self, value):

        self._last = self._alpha*value + (1-self._alpha)*self._last
        return self._last

