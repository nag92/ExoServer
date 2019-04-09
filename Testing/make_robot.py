from Robot import Robot
from Managers import SensorManager, PlotManager, CommunicationManager, FilterManager
from Plotting import Line_Graph

comm = CommunicationManager.CommunicationManager()
SM = SensorManager.SensorManager()
FM = FilterManager.FilterManager()
comm.register_sub(SM)
SM.register_sub(FM)

plotter = PlotManager.PlotManager()
window = PlotManager.PlotManager()
robot = Robot.Robot(SM,FM)

#
#
# accel = robot.get_accel()
# gyro = robot.get_gyro()
# pot = robot.get_pot()
# print pot
# print accel
# plotter.add_pane("Accel", (1,0))
# plotter.add_pane("Gyro",(0,0))
# #plotter.add_pane("POT", (0,0))
# plotter.add_pane("FSR",(0,1))
#
# for ii, sensor in enumerate(accel):
#     accel = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x","y", "z"])
#     plotter.add_window(accel,"Accel",(0,ii) )
#
# for ii, sensor in enumerate(gyro):
#     gyro = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x","y", "z"])
#     plotter.add_window(gyro,"Accel",(1,ii) )
#
# # for ii, sensor in enumerate(pot):
# #     pot = Line_Graph.Line_Graph(sensor.name, sensor, 1, ["z"])
# #     plotter.add_window(pot,"POT",(0,ii) )
#
#
# plotter.start()