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
#from lmfit import minimize, Parameters, Minimizer
from Plotting import Stick_Model, FSR_BarGraph, Line_Graph
from random import *
import ttk
import Manager


class PlotManager(Manager.Manager, Tkinter.Tk):

    def __init__(self):

        Tkinter.Tk.__init__(self)
        super(PlotManager,self).__init__()
        self.panel = ttk.Panedwindow(self)
        self.objects = []
        self.panes = {}


    @property
    def parent(self):
        return self

    def add_pane(self, name, position):
        self.panes[name] = ttk.Labelframe(self, text=name, width=100, height=100).grid(row=position[0], column=position[1])
        #self.panel.add(self.panes[name])


    def add_window(self, graph, panel_name, position):
        """

        :type position: tuple
        """
        print self.panes.keys()
        if panel_name in self.panes.keys():
            graph.initilize(self.panes[panel_name], position)
            self.objects.append(graph.object)

        else:
            print "NOT HERE"

    def refresh(self):

        for obj in self.objects:
            obj.update()

    def start(self):
        #self.panel.pack(expand=1, fill="both")
        self.mainloop()



