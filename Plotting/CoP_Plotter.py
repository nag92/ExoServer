import matplotlib.image as mpimg

from Sensors import Sensor
from TK_Plotter import TK_Plotter


class CoP_Plotter(TK_Plotter):

    def __init__(self, name, left, right):
        """

        :type object: Sensor.Sensor
        """
        self._left = left
        self._right = right
        self.name = name
        self.left_locations = [[103, 56], [44, 73], [72, 294]]
        self.right_locations = [[192, 55], [250, 72], [223, 293]]
        self.img = mpimg.imread("/home/nathaniel/git/exoserver/images/AFO_Foot_Sensor.png")
        super(CoP_Plotter, self).__init__(object, name)

    def initilize(self, root, position):
        """
        Create the plot

        :param root: window to put the plot
        :param position: position in window to put the plot
        :return: None
        """

        self.ax.imshow(self.img)

        self.left, = self.ax.plot([], [], 'rx', lw=10)
        self.right, = self.ax.plot([], [], 'bx', lw=10)
        self.ax.autoscale(False)
        super(CoP_Plotter, self).initilize(root, position)

    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return 1

    def update(self):
        """
        callback to update the plot
        :return: None
        """
        # read the sensor and put it into the queue
        self.ax.imshow(self.img)
        left = self.calc_CoP(self._left, self.left_locations)
        right = self.calc_CoP(self._right, self.right_locations)
        self.left.set_xdata([left[0]])
        self.left.set_ydata([left[1]])

        self.right.set_xdata([right[0]])
        self.right.set_ydata([right[1]])

    def calc_CoP(self, sensor, location):
        """
        calculate the CoP of the foot based on the FSR location
        and force
        CoP_x = sum_i(F_i * x_i)/sum_i(F_i)
        CoP_y = sum_i(F_i * y_i)/sum_i(F_i)
        :return:
        """
        fsrs = sensor

        total_force = 0
        centerX = 0
        centerY = 0

        for fsr, loc in zip(fsrs, location):
            total_force += fsr.get_values()[0]
            centerX += fsr.get_values()[0] * loc[0]
            centerY += fsr.get_values()[0] * loc[1]

        return [centerX / total_force, centerY / total_force]
