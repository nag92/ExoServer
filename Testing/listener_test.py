from Communication import Ethernet
from Managers import SensorManager, PlotManager, FilterManager
from Robot import Robot

path = "/home/nathaniel/git/exoserver/Config/sensor_list.yaml"
comm = Ethernet.Ethernet()
SM = SensorManager.SensorManager()
FM = FilterManager.FilterManager()
SM.register_sub(FM)
plotter = PlotManager.PlotManager()
robot = Robot.Robot(path, SM, FM)

comm.register_sub(SM)

print "\n\n"

comm.start()

while 1:
    for name, sensor in SM.get_sensors().iteritems():
