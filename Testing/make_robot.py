from Robot import Robot
from Managers import SensorManager, PlotManager
from Plotting import Line_Graph


SM = SensorManager.SensorManager()
plotter = PlotManager.PlotManager()
window = PlotManager.PlotManager()
robot = Robot.Robot(SM)

accel = robot.get_accel()
gyro = robot.get_gyro()
pot = robot.get_pot()


plotter.add_pane("Accel")
plotter.add_pane("Plotter")


#accel0 = Line_Graph.Line_Graph( accel[0].name, accel[0], 3, ["x","y", "z"])

#plotter.add_window(accel0,"Accel",(0,0) )
plotter.start()