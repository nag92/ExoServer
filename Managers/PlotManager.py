# import modules that I'm using
import matplotlib

matplotlib.use('TKAgg')
import Tkinter
# import matplotlib.pyplot as pltlib
# lmfit is imported becuase parameters are allowed to depend on each other along with bounds, etc.
# from lmfit import minimize, Parameters, Minimizer
import ttk
import Manager
import time


from PyQt4.uic import loadUiType

from PyQt4 import QtGui, QtCore


from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

Ui_MainWindow, QMainWindow = loadUiType('window.ui')

class PlotManager(QMainWindow, Ui_MainWindow, Manager.Manager ):

    def __init__(self):
        self.index = 0
        print Ui_MainWindow
        super(PlotManager, self).__init__()
        self.count = 0
        self.setupUi(self)
        self.objects = {}
        self.mplfigs.itemClicked.connect(self.changefig)
        fig = Figure()
        self.canvas = FigureCanvas(fig)
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.mplwindow, coordinates=True)
        self.stacked_layout = QtGui.QStackedLayout(self.mplwindow)
        self.stacked_layout.addWidget(self.toolbar)
        self.mplvl.addLayout(self.stacked_layout)

    def changefig(self, item):
        text = str(item.text())
        fig, index = self.objects[text]
        print index
        self.stacked_layout.setCurrentIndex(index)

    def addfig(self, fig):

        fig.initilize(self)
        widget = QtGui.QWidget()
        lay = QtGui.QVBoxLayout(widget)
        lay.addWidget(fig.toolbar)
        lay.addWidget(fig.canvas)
        self.stacked_layout.addWidget(widget)
        self.objects[fig.name] = (fig, self.index)
        self.index = self.index + 1
        self.mplfigs.addItem(fig.name)

    def update(self, data):
        """
        override method called when a message is passed
        :param data: sensors.
        :return: None
        """
        # loop through all the plots and update them
        for key, obj in self.objects.iteritems():
            obj[0].update()

    def refesh(self):
        """
        loop to refresh the plots
        :return:
        """

#        time.sleep(0.1)

        print "update"
        for key, obj in self.objects.iteritems():
            obj[0].flush()

        QtCore.QTimer.singleShot(1, self.refesh)


    def start(self):
        """
        start the main loop of the GUI
        :return:
        """
        print "yo"
        self.show()
        self.refesh()











# class PlotManager(Manager.Manager, Tkinter.Tk):
#     """
#     Handle the updating of the plots
#     """
#     def __init__(self):
#
#         Tkinter.Tk.__init__(self)
#         super(PlotManager, self).__init__()
#         self.panel = ttk.Panedwindow(self)
#         self.objects = []
#         self.panes = {}
#
#     @property
#     def parent(self):
#         return self
#
#     def add_pane(self, name, position):
#         """
#         Add a pane to the window
#         :param name: name of pane
#         :param position: position to place pane
#         :type name: str
#         :type position: tuple
#         :return:
#         """
#         self.panes[name] = ttk.Labelframe(self, text=name, width=100, height=100).grid(row=position[0],
#                                                                                        column=position[1])
#     def add_window(self, graph, panel_name, position):
#         """
#         add a window to the pane
#         :type position: tuple
#         """
#
#         # loop through the panes to find the pane to add the window too
#         if panel_name in self.panes.keys():
#             # initilize the window
#             graph.initilize(self.panes[panel_name], position)
#             self.objects.append(graph)
#         else:
#             print "NOT HERE"
#
#     def update(self, data):
#         """
#         override method called when a message is passed
#         :param data: sensors.
#         :return: None
#         """
#         # loop through all the plots and update them
#         for obj in self.objects:
#             obj.update()
#
#     def refesh(self):
#         """
#         loop to refresh the plots
#         :return:
#         """
#         while 1:
#             time.sleep(0.1)
#             for obj in self.objects:
#                 obj.flush()
#
#     def start(self):
#         """
#         start the main loop of the GUI
#         :return:
#         """
#         self.after(2, self.refesh)  # call the refreash method
#         self.mainloop()
