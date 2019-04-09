
class Subscriber:
    def __init__(self ,callback):
        self._callback = callback

    @property
    def callback(self ,callback):
        self._callback = callback

    @callback.getter
    def callback(self):
        return self._callback
