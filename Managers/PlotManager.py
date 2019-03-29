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


    @property
    def parent(self):
        return self





