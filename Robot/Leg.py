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

    def calc_CoP(self):
        fsrs = self._ankle.FSRs
