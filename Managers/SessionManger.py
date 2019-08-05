import datetime
import os
import time
# from Testing import monitor
from PyQt5 import QtWidgets

import yaml

from Communication import Ethernet
from Managers import Manager, RecorderManager, FilterManager, SensorManager, PlotManager
from QTPlotting import Line_Graph, FSR_BarGraph, CoP_Plotter
from Robot import Robot
from UI import Notes


class SessionManager(Manager.Manager):
    lbls = None  # type: object

    def __init__(self, main, btn, txt, lbl):

        """
              Create the session manager. Each session consits of muiltpy trials
              Each subject should be a new session and be made up of several trials.

             :param btn: list of buttons
             :param txt: list of textboxes
             :param lbl: list of labels
             :type btn: List[QtWidgets.QAbstractButton]
             :type txt: List[QtWidgets.QPlainTextEdit]
             :type lbl: List[QtWidgets.QLabel]
        """

        self.trial_number = 0
        self.session_name = ""
        self.date = datetime.datetime.now()
        self.start_time = None
        self.current_milli_time = lambda: int(round(time.time() * 1000))
        path = "/home/nathaniel/git/exoserver/Config/sensor_list.yaml"
        self.SM = SensorManager.SensorManager()
        self.FM = FilterManager.FilterManager()  # btns = None  # type: Dict[Any, QtWidgets.QAbstractButton]
        #

        # set up Managers
        self.SM.register_sub(self.FM)
        # self.plotter = PlotManager.PlotManager()
        self.robot = Robot.Robot(path, self.SM, self.FM)
        self.sensor_names = self.SM.get_sensor_names()
        self.comm = Ethernet.Ethernet()
        self.comm.register_sub(self.SM)

        self.recorder = RecorderManager.RecorderManager(self.sensor_names)
        self.SM.register_sub(self.recorder)
        self.setup_monitor()
        # turn off the buttons
        self.in_session = False
        self.recording = False
        # make some dicts of the widgets
        self.txt_boxes = self.make_objects(txt)
        self.lbls = self.make_objects(lbl)
        self.btns = self.make_objects(btn)
        # Add callbacks to the buttons
        self.btns["btnStop"].clicked.connect(self.stop_callback)
        self.btns["btnStartSession"].clicked.connect(self.session_callback)
        self.btns["btnRecord"].clicked.connect(self.record_callback)
        self.btns["btnOpenMonitor"].clicked.connect(self.monitor_callback)
        self.btns["btnStartSession"].clicked.connect(self.session_callback)
        self.btns["btnConnect"].clicked.connect(self.connect_callback)
        #self.make_monitor()
        self.main_window = main
        super(SessionManager, self).__init__()

    def make_objects(self, objs):
        """
        Turns the list of widgets into dicts to make accessing them easier

        :param objs:  List[QtWidgets]
        :return: Dict[QtWidgets]
        """
        object_dict = {}
        count = 0
        for obj in objs:
            name = obj.objectName()
            object_dict[name] = obj
            count += 1

        return object_dict

    def session_callback(self):
        """
        Call back for the session button.
        Gets all the data from the subject fields and saves them to
        a yaml file
        :return: None
        """
        print "session"

        # Get the data from the textboxes
        session = {}
        session["Age"] = self.txt_boxes["txtAge"].toPlainText()
        session["Gender"] = self.txt_boxes["txtGender"].toPlainText()
        session["Mass"] = self.txt_boxes["txtMass"].toPlainText()
        session["Height"] = self.txt_boxes["txtHeight"].toPlainText()
        session["LegLength"] = self.txt_boxes["txtLegLength"].toPlainText()
        session["subject"] = self.txt_boxes["txtSubject"].toPlainText()
        session["date"] = self.date
        session["trials"] = {}

        # File name to save data too
        self.session_name = "subject_" + str(session["subject"])
        path = os.path.dirname(os.path.abspath(__file__))

        with open(self.session_name + '.yaml', 'w') as outfile:
            yaml.safe_dump(session, outfile, default_flow_style=False)

        # Enable buttons
        self.in_session = True
        self.btns["btnRecord"].setEnabled(True)
        self.btns["btnStartSession"].setEnabled(False)

    def record_callback(self):
        """
        Callback for the record button
        Start recording the sensors and saving them into a yaml file.
        :return: None
        """
        # Turn on/off the buttons
        self.btns["btnStop"].setEnabled(True)
        self.btns["btnRecord"].setEnabled(False)

        print "record"
        if not self.in_session:
            print "Session not started"
            return

        if self.recorder.recording:
            print "In the middle of recording. Stop the trial first then you can start again"
            return

        # Use the recording manager to save the sensors too.
        trial_name = self.session_name + "_trial_" + str(self.trial_number)
        self.btns["btnRecord"].setStyleSheet("background-color: red")
        self.recorder.new_file(trial_name)
        self.start_time = self.current_milli_time()
        self.recorder.start_recording()

    def setup_monitor(self):
        """
        This sets up all the nessary objects for monitoring the sensors

        :return:
        """
        # Reg
        self.plotter = PlotManager.PlotManager()
        self.SM.register_sub(self.plotter)
        accel = self.robot.get_accel
        gyro = self.robot.get_gyro
        pot = self.robot.get_pot
        fsr = self.robot.get_fsr
        left_fsr = [fsr["FSR1_Left"], fsr["FSR2_Left"], fsr["FSR3_Left"]]
        right_fsr = [fsr["FSR1_Right"], fsr["FSR2_Right"], fsr["FSR3_Right"]]


        for key, sensor in accel.items():
            accel = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
            self.plotter.addfig(accel)

        for key, sensor in gyro.items():
            gyro = Line_Graph.Line_Graph(sensor.name, sensor, 3, ["x", "y", "z"])
            self.plotter.addfig(gyro)

        for key, sensor in pot.items():
            pot = Line_Graph.Line_Graph(sensor.name, sensor, 1, ["z"])
            self.plotter.addfig(pot)

        fsr_plot = FSR_BarGraph.FSR_BarGraph("FSR", fsr.values())
        self.plotter.addfig(fsr_plot)
        #
        cop_plot = CoP_Plotter.CoP_Plotter("CoP", left_fsr, right_fsr)
        self.plotter.addfig(cop_plot)


    def monitor_callback(self):
        """
        Bring up the monitors
        :param button:
        :return:
        """
        self.plotter.start()
        # self.plotter.show()

    def stop_callback(self):
        """
        callback for the stop buton. stops recording of the sensors and
        increaments the trial number.
        :return:
        """

        self.recorder.stop_recording()
        dt = self.current_milli_time() - self.start_time
        print "stop"

        trial_name = self.session_name + "_trial_" + str(self.trial_number)

        dialog = QtWidgets.QDialog()
        dialog.ui = Notes.Notes()
        dialog.ui.setupUi(dialog, trial_name)
        dialog.exec_()
        dialog.show()
        # turn on/off the buttons
        self.btns["btnStop"].setEnabled(False)
        self.btns["btnRecord"].setEnabled(True)
        self.btns["btnRecord"].setStyleSheet("background-color: white")
        # stop the recording


        # update the yaml file
        with open(self.session_name + ".yaml") as f:
            list_doc = yaml.safe_load(f)
        current_trial = {}
        current_trial["dt"] = dt
        current_trial["number"] = self.trial_number
        current_trial["output"] = trial_name + ".yaml"
        current_trial["notes"] = trial_name + "_notes.txt"
        current_trial["vicon"] = "vicon_" + trial_name + ".csv"

        list_doc["trials"][self.trial_number] = current_trial
        with open(self.session_name + ".yaml", "w") as f:
            yaml.safe_dump(list_doc, f)
        # increament the trial number
        self.trial_number = self.trial_number + 1
        self.lbls["lblTrialNumber"].setText("Trial " + str(self.trial_number))

    def connect_callback(self):
        """
        Callback for the connect button.
        Connects to the exoskeleton. It uses the port and host
        boxes to connect.
        :return:
        """
        print "connect"
        self.btns["btnConnect"].setEnabled(False)
        self.btns["btnOpenMonitor"].setEnabled(True)
        host = self.txt_boxes["txtHost"].toPlainText()
        port = int(self.txt_boxes["txtPort"].toPlainText())
        print host
        print port
        self.comm.setup(host, port)
        self.comm.start()
        self.connected = self.comm.connected
