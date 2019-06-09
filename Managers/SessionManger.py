import datetime
import os
from PyQt5 import QtWidgets

import yaml
from typing import List, Any, Dict

from Communication import Ethernet
from Managers import Manager, RecorderManager, FilterManager, SensorManager, PlotManager
from Plotting import Line_Graph, FSR_BarGraph, CoP_Plotter
from Robot import Robot


class SessionManager(Manager.Manager):

    btns = None  # type: Dict[Any, QtWidgets.QAbstractButton]

    txt = None  # type: List[QtWidgets.QPlainTextEdit]

    def __int__(self, btn, txt, lbl):
        path = "/home/nathaniel/git/exoserver/Config/sensor_list.yaml"
        self.SM = SensorManager.SensorManager()
        self.FM = FilterManager.FilterManager()

        self.SM.register_sub(self.FM)

        plotter = PlotManager.PlotManager()
        self.robot = Robot.Robot(path, self.SM, self.FM)
        self.sensor_names = self.SM.get_sensor_names()
        self.comm = Ethernet.Ethernet()
        self.comm.register_sub(self.SM)
        self.SM.register_sub(plotter)
        self.recorder = RecorderManager.RecorderManager(self.sensor_names)
        self.SM.register_sub(self.recorder)
        self.in_session = False
        self.txt_boxes = self.make_objects(txt)
        self.lbls = self.make_objects(lbl)
        self.btns = self.make_objects(btn)


        self.click_functions = {}

        self.trial_number = 0
        self.session_name = ""
        self.date = datetime.datetime.now()

    def make_objects(self, objs):

        object_dict = {}
        for obj in objs:
            name = obj.objectName()
            if obj is QtWidgets.QAbstractButton:
                obj.clicked.connect(lambda: self.on_click(obj))
            object_dict[name] = obj

        return object_dict

    def on_click(self, btn):
        """
        General callback that will handle the function calls to the other
        fuctions. This will make it easier to build the front end because
        only one callback in the front end.
        :param btn:  The button that was clicked
        :type btn:  QtWidgets.QAbstractButton
        :return:
        """
        if btn.objectName() is "btnStartSession":
            self.session_callback()
        if btn.objectName() is "btnStop":
            self.stop_callback()
        if btn.objectName() is "btnRecord":
            self.record_callback()
        if btn.objectName() is "btnOpenMonitor":
            self.monitor_callback()

    def session_callback(self):
        session = {}
        for name, box in self.txt:
            # Error checking is needed
            # maybe used groups???
            value = box.textbox.text()
            session[name] = value

        session["date"] = self.date
        session["trials"] = []

        self.session_name = "subject_" + str(session["subject"])
        path = os.path.dirname(os.path.abspath(__file__))

        with open(self.session_name + '.yaml', 'w') as outfile:
            yaml.dump(session, outfile, default_flow_style=False)

        self.in_session = True

        pass

    def record_callback(self):

        if not self.in_session:
            print "Session not started"
            return

        if self.recorder.recording:
            print "In the middle of recording. Stop the trial first then you can start again"
            return

        trial_name = "trial_" + str(self.trial_number)

        self.btns["btnRecording"].setStyleSheet("background-color: red")
        self.recorder.new_file(trial_name)
        self.recorder.start_recording()

    def monitor_callback(self):
        """
        Bring up the monitors
        :param button:
        :return:
        """
        pass

    def make_monitor(self):

        print "\n\n"
        for name, sensor in self.SM.get_sensors().iteritems():
            print sensor.name, sensor.raw_values

        accel = self.robot.get_accel

        gyro = self.robot.get_gyro
        pot = self.robot.get_pot
        fsr = self.robot.get_fsr

        # print accel
        self.plotter.add_pane("Accel", (0, 0))
        self.plotter.add_pane("Gyro", (0, 0))
        self.plotter.add_pane("Pot", (0, 0))
        self.plotter.add_pane("FSR", (1, 0))
        self.plotter.add_pane("CoP", (0, 0))

        for ii, (key, sensor) in enumerate(accel.iteritems()):
            print type(sensor)
            accel = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
            self.plotter.add_window(accel, "Accel", (0, ii))

        for ii, (key, sensor) in enumerate(gyro.iteritems()):
            gyro = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
            self.plotter.add_window(gyro, "Gyro", (1, ii))

        for ii, (key, sensor) in enumerate(pot.iteritems()):
            print sensor
            item = Line_Graph.Line_Graph(sensor.name, sensor, 1, ["z"])
            plotter.add_window(item, "Pot", (2, ii))

        item = FSR_BarGraph.FSR_BarGraph("FSR", fsr.values())
        self.plotter.add_window(item, "FSR", (2, 6))
        left_fsr = [fsr["FSR1_Left"], fsr["FSR2_Left"], fsr["FSR3_Left"]]
        right_fsr = [fsr["FSR1_Right"], fsr["FSR2_Right"], fsr["FSR3_Right"]]
        item = CoP_Plotter.CoP_Plotter("CoP", left_fsr, right_fsr)
        self.plotter.add_window(item, "CoP", (3, 0))

    def stop_callback(self):

        self.recorder.stop_recording()
        trial_name = "trial_" + str(self.trial_number)

        with open("my_file.yaml") as f:
            list_doc = yaml.load(f)
        list_doc["trials"].append(trial_name)
        with open(self.session_name + ".yaml", "w") as f:
            yaml.dump(list_doc, f)

    def connect_callback(self):

        host = self.txt["txthost"].textbox.text()
        port = self.txt["txtport"].textbox.text()

        self.comm.setup(host, port)
        self.connected = self.comm.connected
