import datetime
import os
from PyQt5 import QtWidgets

import yaml

from Communication import Ethernet
from Managers import Manager, RecorderManager, FilterManager, SensorManager, PlotManager
from Plotting import Line_Graph, FSR_BarGraph, CoP_Plotter
from Robot import Robot


class SessionManager(Manager.Manager):

    #txt_boxes = None  # type: Dict[Any, QtWidgets.QPlainTextEdit]

    def __init__(self, btn, txt, lbl):
        """


        """
        self.trial_number = 0
        self.session_name = ""
        self.date = datetime.datetime.now()



        path = "/home/nathaniel/git/exoserver/Config/sensor_list.yaml"
        self.SM = SensorManager.SensorManager()
        self.FM = FilterManager.FilterManager()  # btns = None  # type: Dict[Any, QtWidgets.QAbstractButton]
        #
        # txt = None  # type: List[QtWidgets.QPlainTextEdit]
        self.SM.register_sub(self.FM)

        self.plotter = PlotManager.PlotManager()
        self.robot = Robot.Robot(path, self.SM, self.FM)
        self.sensor_names = self.SM.get_sensor_names()
        self.comm = Ethernet.Ethernet()
        self.comm.register_sub(self.SM)
        self.SM.register_sub(self.plotter)
        self.recorder = RecorderManager.RecorderManager(self.sensor_names)
        self.SM.register_sub(self.recorder)
        self.in_session = False
        self.txt_boxes = self.make_objects(txt)
        self.lbls = self.make_objects(lbl)
        self.btns = self.make_objects(btn)
        self.btns["btnStop"].clicked.connect(self.stop_callback)
        self.btns["btnStartSession"].clicked.connect(self.session_callback)
        self.btns["btnRecord"].clicked.connect(self.record_callback)
        self.btns["btnOpenMonitor"].clicked.connect(self.monitor_callback)
        self.btns["btnStartSession"].clicked.connect(self.session_callback)
        self.btns["btnConnect"].clicked.connect(self.connect_callback)

        super(SessionManager, self).__init__()

    def make_objects(self, objs):

        object_dict = {}
        count = 0
        for obj in objs:
            name = obj.objectName()
            object_dict[name] = obj
            count+=1

        return object_dict

    def session_callback(self):
        print "session"
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
        print "record"
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
        print "monitoir"
        self.plotter.start()

    def make_monitor(self):


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
            self.plotter.add_window(item, "Pot", (2, ii))

        item = FSR_BarGraph.FSR_BarGraph("FSR", fsr.values())
        self.plotter.add_window(item, "FSR", (2, 6))
        left_fsr = [fsr["FSR1_Left"], fsr["FSR2_Left"], fsr["FSR3_Left"]]
        right_fsr = [fsr["FSR1_Right"], fsr["FSR2_Right"], fsr["FSR3_Right"]]
        item = CoP_Plotter.CoP_Plotter("CoP", left_fsr, right_fsr)
        self.plotter.add_window(item, "CoP", (3, 0))

    def stop_callback(self):
        print "stop"
        # self.recorder.stop_recording()
        # trial_name = "trial_" + str(self.trial_number)
        #
        # with open("my_file.yaml") as f:
        #     list_doc = yaml.load(f)
        # list_doc["trials"].append(trial_name)
        # with open(self.session_name + ".yaml", "w") as f:
        #     yaml.dump(list_doc, f)

    def connect_callback(self):
        print "connect"
        host = self.txt_boxes["txtHost"].toPlainText()
        port = int(self.txt_boxes["txtPort"].toPlainText())
        print host
        print port
        self.comm.setup(host, port)
        self.comm.start()
        self.connected = self.comm.connected
