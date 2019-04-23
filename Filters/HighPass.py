import BaseFilter


class HighPass(BaseFilter.BaseFilter):
    """
    implementation of a high pass filter
    """
    def __init__(self, alpha):
        self._alpha = alpha
        self._x = 0
        self._y = 0
        super(HighPass, self).__init__()

    def update(self, value):
        self._y = self._alpha * (self._y + value - self._x)
        self._x = value
        return self._y
