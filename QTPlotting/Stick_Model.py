from QT_Plotter import QT_Plotter
from Robot import Robot

class Stick_Model(QT_Plotter):

    def __init__(self, object, position, robot):
        assert isinstance(robot, Robot.Robot)
        self._robot = robot
        super(Stick_Model, self).__init__(object)

    def initilize(self, parent):
        """
        Create the plot

        :param root: window to put the plot
        :param position: position in window to put the plot
        :return: None
        """
        self.ax = self.fig.add_subplot(111, autoscale_on=False, xlim=(-1, 1), ylim=(-2, 2))
        self.back_leg, = self.ax.plot([], [], 'bo-', lw=2)
        self.front_leg, = self.ax.plot([], [], 'ro-', lw=2)
        self.trunk, = self.ax.plot([], [], 'go-', lw=2)

        super(Line_Graph, self).initilize(parent)

    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return 1

    def update(self):
        """ update the plot"""
        points, L, R = self._robot.fk()

        legs_x = points["x"]
        legs_y = points["y"]

        self.trunk.set_xdata([legs_x[1], legs_x[2]] )
        self.trunk.set_ydata([legs_y[1], legs_y[2]])
        self.back_leg.set_ydata([legs_y[5], legs_y[6], legs_y[7], R[0][1], R[1][1],legs_y[7]  ])
        self.back_leg.set_xdata([legs_x[5], legs_x[6], legs_x[7], R[0][0], R[1][0],legs_x[7]   ])

        self.front_leg.set_ydata([legs_y[2], legs_y[3], legs_y[4], L[0][1],L[1][1],legs_y[4] ])
        self.front_leg.set_xdata([legs_x[2], legs_x[3], legs_x[4], L[0][0],L[1][0],legs_x[4] ])


        # self.flush()
