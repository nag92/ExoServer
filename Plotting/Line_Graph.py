import abc
from Tkinter import *
from TK_Plotter import TK_Plotter
import numpy as np


class Line_Graph(TK_Plotter):

    def __init__(self, ID, position, num, labels):

        self.num = num
        self.labels = labels
        self.lines = []

        super(Line_Graph, self).__init__(ID)

    def initilize(self, root,position):

        for ii in xrange(self.num):
            self.lines.append(self.ax.plot([], [], self.colors[ii], lw=2))

        self.ax.legend(self.labels, loc='upper left')

        super(Line_Graph, self).initilize(root, position)

    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return 1

    def update(self, data):

        for ii, line in enumerate(self.labels):
            line.set_xdata(data[ii]["x"])
            line.set_ydata(data[ii]["y"])

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
