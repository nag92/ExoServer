import abc
import matplotlib
from Tkinter import *

matplotlib.use('TKAgg')
from Sensors import Sensor
import matplotlib.figure
import matplotlib.pyplot as pltlib


class TK_Plotter(object):

    def __init__(self, object, name):
        """

        :type object: Sensor.Sensor
        """
        self.object = object
        self.name = name
        self.canvasFig = pltlib.figure(1)
        self.fig = matplotlib.figure.Figure(figsize=(3, 2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.autoscale(True, tight=True)
        self.colors = ['r-', 'g-', 'b-', 'k-', 'm-', 'c-', 'y-']
        self.value = None
        self.root = None
        self.position = (0, 0)

    @abc.abstractmethod
    def initilize(self, root, position):
        """
        This function is used to set up the windows
        set up a window to plot
        :param root: window to put the plot in
        :param position: where to put the window
        :return: None
        """

        self.root = root
        self.position = position
        self.frame = Frame(self.root)
        self.frame.grid(row=self.position[0], column=self.position[1])
        self.set_title(self.name)
        self.set_axis_names()
        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=0)
        # self.set_fitler_menu()
        return

    @abc.abstractmethod
    def update(self):
        """
        override function to be called to update the plot
        :return:
        """
        pass

    def set_title(self, title="some_graph"):
        """
        set the title of the plot
        :param title: name of the plot
        :type: str
        :return:
        """
        self.ax.set_title(title)
        return

    def set_axis_names(self, x="x", y="y"):
        """
        set the axis names
        :param x: name of x axis
        :param y: name of y axis
        :type x: str
        :type y: str
        :return:
        """
        self.ax.set_xlabel(x)
        self.ax.set_ylabel(y)

    def flush(self):
        """
        Update the plot graphics
        :return:
        """
        # update the axis limits
        self.ax.relim()
        self.ax.autoscale_view()
        #redraw
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
