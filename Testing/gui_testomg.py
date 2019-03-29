import matplotlib
matplotlib.use('TKAgg')
import Tkinter
from Plotting import Stick_Model, FSR_BarGraph, Line_Graph
from Sensors import Sensor, Accel, FSR
from Plotting import TK_Plotter
#Make object for application
import ttk


from Managers import PlotManager

class App_Window(Tkinter.Tk):

    def __init__(self, panels, parent=None):

        assert isinstance(panels, list(TK_Plotter.TK_Plotter))
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.panels = panels
        self.view = False
        self.initialize()

    def initialize(self):

        for key, value in self.panel.iteritems():
            value.initilize(self)


    def refresh(self):

        for panel in self.panels:
            panel.update()

    def OnButtonClick(self):
        pass


if __name__ == "__main__":


    window = PlotManager.PlotManager()

    fsr1 = FSR.FSR("one")
    fsr2 = FSR.FSR("two")
    fsr3 = FSR.FSR("three")

    p = ttk.Panedwindow(window.parent)
    # first pane, which would get widgets gridded into it:
    fsr_frame = ttk.Labelframe(p, text='FSR', width=100, height=100)
    pot_frame = ttk.Labelframe(p, text='POT', width=100, height=100)
    imu_frame = ttk.Labelframe(p, text='POT', width=100, height=100)
    stick_frame = ttk.Labelframe(p, text='stick', width=100, height=100)


    p.add(fsr_frame)
    p.add(pot_frame)
    p.add(imu_frame)
    p.add(stick_frame)

    #stick = Stick_Model.Stick_Model(stick_frame, (0, 0))
    #bars = FSR_BarGraph.FSR_BarGraph(fsr_frame, (0, 1), 6)

    # self.line = Line_Graph.Line_Graph(self, (0, 0), 3, ["sdf", "sags", "agsd"])


    bars = FSR_BarGraph.FSR_BarGraph([fsr1,fsr2,fsr3], 6)
    line = Line_Graph.Line_Graph(2,  3, ["sdf", "sags", "agsd"])
    p.pack(expand=1, fill="both")


    panels = {}
    panels[0] = bars
    panels[1] = line
    #MainWindow = App_Window(panels)
    #MainWindow.mainloop()