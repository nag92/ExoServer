import time

from Communication import Ethernet
from Managers import SensorManager, PlotManager, FilterManager
from Plotting import Line_Graph, FSR_BarGraph
from Robot import Robot

path = "/home/nathaniel/git/exoserver/Config/sensor_list.yaml"
SM = SensorManager.SensorManager()
FM = FilterManager.FilterManager()

SM.register_sub(FM)

plotter = PlotManager.PlotManager()
robot = Robot.Robot(path, SM, FM)
comm = Ethernet.Ethernet()
comm.register_sub(SM)
SM.register_sub(plotter)
comm.start()


print "\n\n"
for name, sensor in SM.get_sensors().iteritems():
    print sensor.name, sensor.raw_values


#
#
accel = robot.get_accel()
print accel
gyro = robot.get_gyro()
pot = robot.get_pot()
fsr = robot.get_fsr()
time.sleep(3)
print accel
plotter.add_pane("Accel", (0, 0))
plotter.add_pane("Gyro", (0, 0))
plotter.add_pane("Pot", (0, 0))
plotter.add_pane("FSR", (1, 0))

for ii, (key, sensor) in enumerate(accel.iteritems()):
    print type(sensor)
    accel = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
    plotter.add_window(accel, "Accel", (0, ii))

for ii, (key, sensor) in enumerate(gyro.iteritems()):
    gyro = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
    plotter.add_window(gyro, "Gyro", (1, ii))

for ii, (key, sensor) in enumerate(pot.iteritems()):
    print sensor
    item = Line_Graph.Line_Graph(sensor.name, sensor, 1, ["z"])
    plotter.add_window(item, "Pot", (2, ii))

item = FSR_BarGraph.FSR_BarGraph("FSR", fsr.values())
plotter.add_window(item, "FSR", (2, 6))


plotter.start()
