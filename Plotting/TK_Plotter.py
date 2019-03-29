from Tkinter import *
import abc
import matplotlib
matplotlib.use('TKAgg')
from Sensors import Sensor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as pltlib

class TK_Plotter(object):

    def __init__(self, object, root, position ):
        """

        :type object: Sensor.Sensor
        """
        self.object = object
        self.position = position
        self.root = root
        self.canvasFig = pltlib.figure(1)
        self.fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.colors = ['r-', 'g-','b-','k-','m-','c-', 'y-']
        self.value = None


    @abc.abstractmethod
    def initilize(self, root, position):

        """Retrieve data from the input source and return an object."""

        self.frame = Frame(self.root)
        self.frame.grid(row=self.position[0], column=self.position[1])
        self.set_title()
        self.set_axis_names()
        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, column=0)
        #self.set_fitler_menu()
        return

    @abc.abstractmethod
    def update(self):

        """Save the data object to the output."""

        pass


    def set_fitler_menu(self, filters=None):

        pass


    def set_title(self, title="some_graph"):
        self.ax.set_title(title)
        return


    def set_axis_names(self, x="x", y="y"):
        self.ax.set_xlabel(x)
        self.ax.set_ylabel(y)

    def flush(self):
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

