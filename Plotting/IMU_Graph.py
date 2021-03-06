import Queue

import numpy as np

from TK_Plotter import TK_Plotter


class IMU_Graph(TK_Plotter):

    def __init__(self, name, object, num, labels):

        self.num = num
        self.name = name
        self.labels = labels
        self.lines = []
        self.queue_size = 100
        self.ticks = 0
        self.queue = Queue.Queue()
        super(IMU_Graph, self).__init__(object, name)

    def initilize(self, root, position):
        """
        Create the plot

        :param root: window to put the plot
        :param position: position in window to put the plot
        :return: None
        """

        for ii in xrange(self.num):
            self.lines.append(self.ax.plot([], [], self.colors[ii], lw=2))

        self.ax.legend(self.labels, loc='upper left')

        super(IMU_Graph, self).initilize(root, position)

    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return 1

    def update(self):
        """
        callback for to update the plot with new data
        :return:
        """
        # read the sensor and put it into the queue
        values = self.object.orentation()
        self.queue.put(values)

        # get the x axis numbers
        # start it at 0 and go the the number of ticks then
        # once it reachs the queue size then contine the number of readings
        self.ticks = self.ticks + 1
        start = 0
        items = np.array(list(self.queue.queue))
        if self.ticks - self.queue_size > 0:
            start = self.ticks - self.queue_size

        x_data = range(start, self.ticks)

        # update the graph
        for ii, line in enumerate(self.labels):
            line.set_xdata(x_data)
            line.set_ydata(items[:, ii])

        # self.flush()
