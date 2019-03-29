from Robot import Robot
from Managers import SensorManager, PlotManager

SM = SensorManager.SensorManager()
window = PlotManager.PlotManager()
robot = Robot.Robot(SM)

