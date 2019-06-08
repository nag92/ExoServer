import datetime
import os
from PyQt5 import QtWidgets

import yaml
from typing import List, Any, Dict

from Communication import Ethernet
from Managers import Manager, RecorderManager, FilterManager, SensorManager, PlotManager
from Robot import Robot


class SessionManager(Manager.Manager):

    btns = None  # type: Dict[Any, QtWidgets.QAbstractButton]
    # self.textbox.setText("")
    text_boxes = None  # type: List[QtWidgets.QPlainTextEdit]

    def __int__(self):
        path = "/home/nathaniel/git/exoserver/Config/sensor_list.yaml"
        self.SM = SensorManager.SensorManager()
        self.FM = FilterManager.FilterManager()

        self.SM.register_sub(self.FM)

        plotter = PlotManager.PlotManager()
        robot = Robot.Robot(path, self.SM, self.FM)
        self.sensor_names = self.SM.get_sensor_names()
        comm = Ethernet.Ethernet()
        comm.register_sub(self.SM)
        self.SM.register_sub(plotter)
        self.recorder = RecorderManager.RecorderManager(self.sensor_names)
        self.SM.register_sub(self.recorder)
        self.in_session = False
        self.txt_boxes = {}
        self.lbls = {}
        self.btns = {}
        self.trial_number = 0
        self.session_name = ""
        self.date = datetime.datetime.now()

        pass

    def on_click(self, btn):
        """
        General callback that will handle the function calls to the other
        fuctions. This will make it easier to build the front end because
        only one callback in the front end.
        :param btn:
        :return:
        """
        pass

    def session_callback(self):
        session = {}
        for name, box in self.text_boxes:

            value = box.textbox.text()

            # Check if the box has a value
            if value is "":
                RuntimeError("missing value")
                return
            else:
                session[name] = value

        session["date"] = self.date
        session["trials"] = []

        self.session_name = "subject_" + str(session["subject"])
        path = os.path.dirname(os.path.abspath(__file__))

        with open(self.session_name + '.yaml', 'w') as outfile:
            yaml.dump(session, outfile, default_flow_style=False)

        self.in_session = True

        pass

    def record_callback(self, button):

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

    def monitor_callback(self, button):
        """
        Bring up the monitors
        :param button:
        :return:
        """
        pass

    def stop_callback(self, button):
        self.recorder.stop_recording()

        trial_name = "trial_" + str(self.trial_number)

        with open("my_file.yaml") as f:
            list_doc = yaml.load(f)
        list_doc["trials"].append(trial_name)
        with open(self.session_name + ".yaml", "w") as f:
            yaml.dump(list_doc, f)

        self.trial_number += 1
        self.lbls["lblTrialNumber"].setText("Trial " + str(self.trial_number))


        pass

