import Queue
from Tkinter import *

import numpy as np

from Sensors import Sensor
from TK_Plotter import TK_Plotter


class Line_Graph(TK_Plotter):

    def __init__(self, name, object, num, labels):
        """

        :type object: Sensor.Sensor
        """
        self.num = num
        self.name = name
        self.labels = labels
        self.lines = []
        self.queue_size = 100
        self.ticks = 0
        self.queue = Queue.Queue()
        super(Line_Graph, self).__init__(object, name)

    def initilize(self, root, position):

        for ii in xrange(self.num):
            line, = self.ax.plot([], [], self.colors[ii], lw=2)
            self.lines.append(line)

        self.ax.legend(self.labels, loc='upper left')

        super(Line_Graph, self).initilize(root, position)

    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return 1

    def update(self):

        # read the sensor and put it into the queue
        values = self.object.get_values()

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
        print items[:, 0]
        # update the graph
        for ii, line in enumerate(self.lines):
            line.set_xdata(x_data)
            line.set_ydata(items[:, ii])
            # line.set_xdata([0,.1,.2])
            # line.set_ydata([0, 0.05, .01])
            self.flush()

    def set_fitler_menu(self, filters=None):
        self.value = StringVar()
        #
        # frame = Frame(self.frame)
        # frame.grid(row=0, column=1)
        # for index, filter in enumerate(filters):
        #     button = Radiobutton(frame, text=filter,
        #                          variable=self.value,
        #                          value=filter)
        #
        #     button.grid(row=index, column=0)

        # super(Line_Graph, self).set_fitler_menu()
