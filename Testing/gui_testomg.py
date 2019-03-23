import matplotlib
matplotlib.use('TKAgg')
import Tkinter
from Plotting import Stick_Model, FSR_BarGraph, Line_Graph



#Make object for application
class App_Window(Tkinter.Tk):

    def __init__(self, panels, parent=None):

        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.panel = panels
        self.view = False
        self.initialize()

    def initialize(self):

        for key, value in self.panel.iteritems():
            value.initilize(self)


    def refresh(self):

        if not self.view:
            pass
            # for id in self.server.getID():
            #     if id in self.panels.keys():
            #        self.panel[id].update(self.server.getdata(id))
            #

    def OnButtonClick(self):
        pass


if __name__ == "__main__":


    stick = Stick_Model.Stick_Model(0)
    bars = FSR_BarGraph.FSR_BarGraph(1, 6)
    line = Line_Graph.Line_Graph(2,  3, ["sdf", "sags", "agsd"])
    panels = {}

    panels[0] = stick
    panels[1] = bars
    panels[2] = line
    MainWindow = App_Window(panels)
    MainWindow.mainloop()