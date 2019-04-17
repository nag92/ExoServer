import yaml

from Filters import BaseFilter
from Managers import SensorManager, FilterManager
import Leg, Joint
from Sensors import Accel, Gyro, Pot, FSR, Temperature
from Sensors import IMU


class Robot(object):

    def __init__(self, config_path, SM, FM):

        self._sensor_names = []
        self.sensors = {}
        self._pots = {}
        self._imus = {}
        self._fsr = {}
        self.right_leg = None
        self.left_leg = None
        assert isinstance(SM, SensorManager.SensorManager)
        assert isinstance(FM, FilterManager.FilterManager)
        self._sensor_manager = SM
        self._filter_manager = FM
        self._sensor_manager.register_sub(FM)
        self.__setup_sensors(config_path)

    def __setup_sensors(self, config_path):

        # TODO: add yaml config setup  here

        with open(config_path, "r") as loader:
            config = yaml.load(loader)
            # set up raw sensors
            print config

            for name in config:

                item = config[name]
                byte_list = [item.get("block1"), item.get("block2")]
                sensor_type = item.get("type")
                location = item.get("location")
                side = item.get("side")
                axis = item.get("axis")


                if sensor_type == "Accel":

                    self.sensors[name] = Accel.Accel(name, byte_list, side)
                elif sensor_type == "Gyro":
                    self.sensors[name] = Gyro.Gyro(name, byte_list, side)
                elif sensor_type == "FSR":
                    self.sensors[name] = FSR.FSR(name, byte_list, side)
                elif sensor_type == "Pot":
                    self.sensors[name] = Pot.Pot(name, byte_list, side)
                elif sensor_type == "Temperture":
                    self.sensors[name] = Temperature.Temperature(name, byte_list, side)
                elif sensor_type == "rshal":
                    pass
                pass

            # set up IMUs
            for name in config:
                item = config[name]
                if name == "IMU":
                    accel = item.get("accel")
                    gyro = item.get("gyro")
                    temp = item.get("temp")
                    counter = item.get("counter")
                    rshal = item.get("rshal")
                    imu = IMU.IMU(name,
                                  self.sensors[accel],
                                  self.sensors[gyro],
                                  self.sensors[temp],
                                  self.sensors[counter],
                                  self.sensors[rshal])

                    self._imus[name] = imu
        self._sensor_manager.registar_all_sensors(self.sensors.values())
        print self._sensor_manager.get_sensors()
        # for key, sensor in self.sensors.iteritems():
        #     self._filter_manager.registar([BaseFilter.BaseFilter(sensor)], sensor)

    def __setup_robot(self):

        right_hip = Joint.Joint(self._imus["IMU_Right_Hip"], self.sensors["Pot_Right_Hip"])
        right_knee = Joint.Joint(self._imus["IMU_Right_Knee"], self.sensors["Pot_Right_Knee"])
        fsr = [self.sensors["FSR1_Right"], self.sensors["FSR2_Right"], self.sensors["FSR3_Right"]]
        right_ankle = Joint.Joint(self._imus["IMU_Right_Ankle"], self.sensors["Pot_Right_Ankle"], fsr)
        self.right_leg = Leg.Leg(right_hip, right_knee, right_ankle)

        left_hip = Joint.Joint(self._imus["IMU_Left_Hip"], self.sensors["Pot_Left_Hip"])
        left_knee = Joint.Joint(self._imus["IMU_Left_Knee"], self.sensors["Pot_Left_Knee"])
        fsr = [self.sensors["FSR1_Left"], self.sensors["FSR2_Left"], self.sensors["FSR3_Left"]]
        left_ankle = Joint.Joint(self._imus["IMU_Left_Ankle"], self.sensors["Pot_Left_Ankle"], fsr)
        self.left_leg = Leg.Leg(left_hip, left_knee, left_ankle)

    @property
    def sensor_names(self):
        return self._sensor_names


    def get_imus(self):
        return self._imus

    def get_accel(self):
        data = {}
        for key, value in self.sensors.iteritems():
            if "Accel" in key:
                data[key] = value

        return data

    def get_gyro(self):
        data = {}
        for key, value in self.sensors.iteritems():
            if "Gyro" in key:
                data[key] = value

        return data

    def get_pot(self):
        data = {}
        for key, value in self.sensors.iteritems():
            if "POT" in key:
                data[key] = value

        return data

    def get_fsr(self):
        data = {}
        for key, value in self.sensors.iteritems():
            if "FSR" in key:
                data[key] = value

        return data
