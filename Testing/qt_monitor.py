from PyQt5 import QtWidgets
import sys
from PyQt5 import QtWidgets

from Communication import Ethernet
from Managers import SensorManager, PlotManager, FilterManager
from QTPlotting import Line_Graph
from Robot import Robot

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    path = "/home/nathaniel/git/exoserver/Config/sensor_list.yaml"
    SM = SensorManager.SensorManager()
    FM = FilterManager.FilterManager()

    SM.register_sub(FM)

    plotter = PlotManager.PlotManager()
    robot = Robot.Robot(path, SM, FM)
    names = SM.get_sensor_names()
    comm = Ethernet.Ethernet()
    comm.setup()
    comm.register_sub(SM)
    SM.register_sub(plotter)

    for name, sensor in SM.get_sensors().iteritems():
        print sensor.name, sensor.raw_values

    accel = robot.get_accel
    gyro = robot.get_gyro
    pot = robot.get_pot
    fsr = robot.get_fsr

    for key, sensor in accel.items():
        accel = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
        plotter.addfig(accel)
    # print accel
    # plotter.add_pane("Accel", (0, 0))
    # plotter.add_pane("Gyro", (0, 0))
    # plotter.add_pane("Pot", (0, 0))
    # plotter.add_pane("FSR", (1, 0))
    # plotter.add_pane("CoP", (0, 0))
    #
    # for ii, (key, sensor) in enumerate(accel.iteritems()):
    #     print type(sensor)
    #     accel = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
    #     plotter.add_window(accel, "Accel", (0, ii))
    #
    # for ii, (key, sensor) in enumerate(gyro.iteritems()):
    #     gyro = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
    #     plotter.add_window(gyro, "Gyro", (1, ii))
    #
    # for ii, (key, sensor) in enumerate(pot.iteritems()):
    #     print sensor
    #     item = Line_Graph.Line_Graph(sensor.name, sensor, 1, ["z"])
    #     plotter.add_window(item, "Pot", (2, ii))
    #
    # item = FSR_BarGraph.FSR_BarGraph("FSR", fsr.values())
    # plotter.add_window(item, "FSR", (2, 6))
    # left_fsr = [fsr["FSR1_Left"], fsr["FSR2_Left"], fsr["FSR3_Left"]]
    # right_fsr = [fsr["FSR1_Right"], fsr["FSR2_Right"], fsr["FSR3_Right"]]
    # item = CoP_Plotter.CoP_Plotter("CoP", left_fsr, right_fsr)
    # plotter.add_window(item, "CoP", (3, 0))


    comm.start()
    plotter.start()
    plotter.show()
    sys.exit(app.exec_())

