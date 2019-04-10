from Managers import SensorManager, PlotManager
from Plotting import Line_Graph, IMU_Graph, FSR_BarGraph
from Robot import Robot

SM = SensorManager.SensorManager()
plotter = PlotManager.PlotManager()
window = PlotManager.PlotManager()
robot = Robot.Robot(SM)

accel = robot.get_accel()
gyro = robot.get_gyro()
pot = robot.get_pot()
imus = robot.get_imus()
fsr = robot.get_fsr()

plotter.add_pane("Hip", (0, 0))
plotter.add_pane("Knee", (1, 0))
plotter.add_pane("Ankle", (2, 0))

imu = IMU_Graph.IMU_Graph("IMU_Right_Hip", imus["IMU_Right_Hip"], 3, ["x", "y", "z"])
plotter.add_window(imu, "Hip", (0, 0))

imu = IMU_Graph.IMU_Graph("IMU_Right_Knee", imus["IMU_Right_Knee"], 3, ["x", "y", "z"])
plotter.add_window(imu, "Knee", (1, 0))

imu = IMU_Graph.IMU_Graph("IMU_Right_Ankle", imus["IMU_Right_Ankle"], 3, ["x", "y", "z"])
plotter.add_window(imu, "Ankle", (2, 0))

imu = IMU_Graph.IMU_Graph("IMU_Left_Hip", imus["IMU_Left_Hip"], 3, ["x", "y", "z"])
plotter.add_window(imu, "Hip", (0, 1))

imu = IMU_Graph.IMU_Graph("IMU_Left_Knee", imus["IMU_Left_Knee"], 3, ["x", "y", "z"])
plotter.add_window(imu, "Knee", (1, 1))

imu = IMU_Graph.IMU_Graph("IMU_Left_Ankle", imus["IMU_Left_Ankle"], 3, ["x", "y", "z"])
plotter.add_window(imu, "Ankle", (2, 1))

for key, sensor in pot.iteritems():

    pot = Line_Graph.Line_Graph(key, sensor, 1, ["z"])

    if "Hip" in key:
        index = 0
        joint = "Hip"
    elif "Knee" in key:
        index = 1
        joint = "Knee"
    else:
        index = 2
        joint = "Ankle"

    plotter.add_window(pot, joint, (index, 2))

sensors = fsr.values()
fsr = FSR_BarGraph.FSR_BarGraph("FSR", sensors)
plotter.add_window(fsr, "Ankle", (0, 3))

plotter.start()
