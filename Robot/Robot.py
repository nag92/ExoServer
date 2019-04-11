import yaml

from Filters import BaseFilter
from Managers import SensorManager, FilterManager
import Leg, Joint
from Sensors import Accel, Gyro, Pot, FSR, Temperature
from Sensors import IMU


class Robot(object):

    def __init__(self, config_path, SM, FM):
        config = yaml.load(config_path)
        self._sensor_names = []
        self._sensors = {}
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
        self.__setup_sensors(config)

    def __setup_sensors(self, config):

        # TODO: add yaml config setup  here

        # set up raw sensors
        for name, item in config:
            byte_list = [item["block1"], item["block2"]]
            type = item["type"]
            location = item["location"]
            side = item["side"]
            axis = item["axis"]
            if type is "Accel":
                self._sensors[name] = Accel.Accel(name, byte_list, side)
            elif type is "Gyro":
                self._sensors[name] = Gyro.Gyro(name, byte_list, side)
            elif type is "FSR":
                self._sensors[name] = FSR.FSR(name, byte_list, side)
            elif type is "Pot":
                self._sensors[name] = Pot.Pot(name, byte_list, side)
            elif type is "Temperture":
                self._sensors[name] = Temperature.Temperature(name, byte_list, side)
            elif type is "rshal":
                pass
            pass


        # set up IMUs
        for name, item in config:

            if name is "IMU":
                accel = item["accel"]
                gyro = item["gyro"]
                temp = item["temp"]
                counter = None  # item["counter"]
                rshal = None  # item["rshal"]
                imu = IMU.IMU(name,
                              self._sensors[accel],
                              self._sensors[gyro],
                              self._sensors[temp],
                              self._sensors[counter],
                              self._sensors[rshal])

                self._imus[name] = imu


        self._sensor_manager.registar_all_sensors(self._sensors.values())

        for key, sensor in self._sensors.iteritems():
            self._filter_manager.registar([BaseFilter.BaseFilter(sensor)], sensor)

    def __setup_robot(self):

        right_hip = Joint.Joint(self._imus["IMU_Right_Hip"], self._sensors["Pot_Right_Hip"])
        right_knee = Joint.Joint(self._imus["IMU_Right_Knee"], self._sensors["Pot_Right_Knee"])
        fsr = [self._sensors["FSR1_Right"], self._sensors["FSR2_Right"], self._sensors["FSR3_Right"]]
        right_ankle = Joint.Joint(self._imus["IMU_Right_Ankle"], self._sensors["Pot_Right_Ankle"], fsr)
        self.right_leg = Leg.Leg(right_hip, right_knee, right_ankle)

        left_hip = Joint.Joint(self._imus["IMU_Left_Hip"], self._sensors["Pot_Left_Hip"])
        left_knee = Joint.Joint(self._imus["IMU_Left_Knee"], self._sensors["Pot_Left_Knee"])
        fsr = [self._sensors["FSR1_Left"], self._sensors["FSR2_Left"], self._sensors["FSR3_Left"]]
        left_ankle = Joint.Joint(self._imus["IMU_Left_Ankle"], self._sensors["Pot_Left_Ankle"], fsr)
        self.left_leg = Leg.Leg(left_hip, left_knee, left_ankle)

    @property
    def sensor_names(self):
        return self._sensor_names

    @sensor_names.setter
    def sensor_names(self, value):
        self._sensor_names = value

    @property
    def sensors(self):
        return self._sensor_names

    @sensors.setter
    def sensors(self, value):
        self._sensors = value

    def get_imus(self):
        return self._imus

    def get_accel(self):
        data = {}
        for key, value in self._sensors.iteritems():
            if "Accel" in key:
                data[key] = value

        return data

    def get_gyro(self):
        data = {}
        for key, value in self._sensors.iteritems():
            if "Gyro" in key:
                data[key] = value

        return data

    def get_pot(self):
        data = {}
        for key, value in self._sensors.iteritems():
            if "POT" in key:
                data[key] = value

        return data

    def get_fsr(self):
        data = {}
        for key, value in self._sensors.iteritems():
            if "FSR" in key:
                data[key] = value

        return data
