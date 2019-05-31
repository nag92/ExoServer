import Joint
class Leg(object):


    def __init__(self, hip, knee, ankle):
        """

        :param hip:
        :param knee:
        :param ankle:
        :type ankle: Joint.Joint
        """
        self._hip = hip
        self._knee = knee
        self._ankle = ankle
        self._CoP = [0, 0]

    @property
    def CoP(self):
        return self._CoP

    @CoP.setter
    def CoP(self, value):
        self._CoP = value

    def calc_CoP(self):
        fsrs = self._ankle.FSRs

        total_force = 0
        centerX = 0
        centerY = 0

        for sensor in fsrs:
            total_force += sensor.get_values()
            centerX += sensor.get_values() * sensor.orientation[0]
            centerY += sensor.get_values() * sensor.orientation[1]

        self._CoP = [centerX / total_force, centerY / total_force]
