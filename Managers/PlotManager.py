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


class PlotManager(Manager.Manager, Tkinter.Tk):
    """
    Handle the updating of the plots
    """
    def __init__(self):

        Tkinter.Tk.__init__(self)
        super(PlotManager, self).__init__()
        self.panel = ttk.Panedwindow(self)
        self.objects = []
        self.panes = {}

    @property
    def parent(self):
        return self

    def add_pane(self, name, position):
        """
        Add a pane to the window
        :param name: name of pane
        :param position: position to place pane
        :type name: str
        :type position: tuple
        :return:
        """
        self.panes[name] = ttk.Labelframe(self, text=name, width=100, height=100).grid(row=position[0],
                                                                                       column=position[1])
    def add_window(self, graph, panel_name, position):
        """
        add a window to the pane
        :type position: tuple
        """

        # loop through the panes to find the pane to add the window too
        if panel_name in self.panes.keys():
            # initilize the window
            graph.initilize(self.panes[panel_name], position)
            self.objects.append(graph)
        else:
            print "NOT HERE"

    def update(self, data):
        """
        override method called when a message is passed
        :param data: sensors.
        :return: None
        """
        # loop through all the plots and update them
        for obj in self.objects:
            obj.update()

    def refesh(self):
        """
        loop to refresh the plots
        :return:
        """
        while 1:
            time.sleep(0.1)
            for obj in self.objects:
                obj.flush()

    def start(self):
        """
        start the main loop of the GUI
        :return:
        """
        self.after(2, self.refesh)  # call the refreash method
        self.mainloop()
