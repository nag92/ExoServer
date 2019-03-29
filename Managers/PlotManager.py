# import modules that I'm using
import matplotlib
matplotlib.use('TKAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as pltlib
import Tkinter
from Tkinter import *
import numpy as np
import scipy as sc
#import matplotlib.pyplot as pltlib
# lmfit is imported becuase parameters are allowed to depend on each other along with bounds, etc.
from lmfit import minimize, Parameters, Minimizer
from Plotting import Stick_Model, FSR_BarGraph, Line_Graph
from random import *
import ttk
import Manager


class PlotManager(Tkinter.Tk):

    def __init__(self):

        Tkinter.Tk.__init__(self)
        self.panel = ttk.Panedwindow(self.parent)
        self._objects = []
        self.panes = {}


    @property
    def parent(self):
        return self

    def add_pane(self, name):
        self.panes[name] = ttk.Labelframe(self.panel, text=name, width=100, height=100)
        self.panel.add(self.panes[name])


    def add_window(self, graph, panel_name, position):
        """

        :type position: tuple
        """
        if panel_name in self.panes.keys():

            graph.initilize(self.panes[panel_name], position)
            self._objects.append(graph.object)

        else:
            RuntimeError

    def start(self):
        self.mainloop()



