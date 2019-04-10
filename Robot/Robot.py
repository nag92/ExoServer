from Managers import SensorManager, FilterManager
from Filters import BaseFilter
from Sensors import Accel, Gyro, Pot, FSR
from Sensors import IMU
import Leg, Joint
import yaml


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

    def __setup_sensors(self,config):

        #TODO: add yaml config setup  here

        for name, item in config:
            byte_list = [item.block1, item.block2]
            type = item.type
            location = item.location
            side = item.side
            axis = item.axis
            if name is "Accel":
                pass
            elif name is "Gyro":
                pass
            elif name is "FSR":
                pass
            elif name is "Pot":
                pass
            elif name is "Temperture":
                pass
            elif name is "rshal":
                pass
            pass

        self._sensor_names = ("IMU_Accel_Left_Foot",
                              "IMU_Gyro_Left_Foot",
                              "IMU_Accel_Right_Foot",
                              "IMU_Gyro_Right_Foot",
                              "IMU_Accel_Left_Knee",
                              "IMU_Gyro_Left_Knee",
                              "IMU_Accel_Right_Knee",
                              "IMU_Gyro_Right_Knee",
                              "IMU_Accel_Left_Knee",
                              "IMU_Gyro_Left_Knee",
                              "IMU_Accel_Right_Hip",
                              "IMU_Gyro_Right_Hip",
                              "IMU_Accel_Center",
                              "IMU_Gyro_Center",
                              "POT_Left_Ankle",
                              "POT_Right_Ankle",
                              "POT_Left_Knee",
                              "POT_Right_Knee",
                              "POT_Left_Hip",
                              "POT_Right_Hip",
                              "FSR_Right_01",
                              "FSR_Right_02",
                              "FSR_Right_03",
                              "FSR_Left_01",
                              "FSR_Left_02",
                              "FSR_Left_03"
                              )

        # IMU Ankle
        self._sensors[self._sensor_names[0]] = Accel.Accel(self._sensor_names[0])
        self._sensors[self._sensor_names[1]] = Gyro.Gyro(self._sensor_names[1])
        self._sensors[self._sensor_names[2]] = Accel.Accel(self._sensor_names[2])
        self._sensors[self._sensor_names[3]] = Gyro.Gyro(self._sensor_names[3])

        imu_left_ankle = IMU.IMU("IMU_Left_Ankle", self._sensors[self._sensor_names[0]],
                                 self._sensors[self._sensor_names[1]])
        imu_right_ankle = IMU.IMU("IMU_Right_Ankle", self._sensors[self._sensor_names[0]],
                                  self._sensors[self._sensor_names[1]])

        self._imus["IMU_Left_Ankle"] = imu_left_ankle
        self._imus["IMU_Right_Ankle"] = imu_right_ankle

        # IMU Knee
        self._sensors[self._sensor_names[4]] = Accel.Accel(self._sensor_names[4])
        self._sensors[self._sensor_names[5]] = Gyro.Gyro(self._sensor_names[5])
        self._sensors[self._sensor_names[6]] = Accel.Accel(self._sensor_names[6])
        self._sensors[self._sensor_names[7]] = Gyro.Gyro(self._sensor_names[7])

        imu_left_knee = IMU.IMU("IMU_Left_Ankle", self._sensors[self._sensor_names[4]],
                                                  self._sensors[self._sensor_names[5]])

        imu_right_knee = IMU.IMU("IMU_Right_Ankle", self._sensors[self._sensor_names[6]],
                                                    self._sensors[self._sensor_names[7]])

        self._imus["IMU_Left_Knee"] = imu_left_knee
        self._imus["IMU_Right_Knee"] = imu_right_knee

        # IMU Hip
        self._sensors[self._sensor_names[8]] = Accel.Accel(self._sensor_names[8])
        self._sensors[self._sensor_names[9]] = Gyro.Gyro(self._sensor_names[9])
        self._sensors[self._sensor_names[10]] = Accel.Accel(self._sensor_names[10])
        self._sensors[self._sensor_names[11]] = Gyro.Gyro(self._sensor_names[11])

        imu_left_hip = IMU.IMU("IMU_Left_Hip", self._sensors[self._sensor_names[8]],
                                               self._sensors[self._sensor_names[9]])

        imu_right_hip = IMU.IMU("IMU_Right_Hip", self._sensors[self._sensor_names[10]],
                                                 self._sensors[self._sensor_names[11]])

        self._imus["IMU_Left_Hip"] = imu_left_hip
        self._imus["IMU_Right_Hip"] = imu_right_hip

        # IMU Center
        self._sensors[self._sensor_names[12]] = Accel.Accel(self._sensor_names[12])
        self._sensors[self._sensor_names[13]] = Gyro.Gyro(self._sensor_names[13])

        imu_center = IMU.IMU("IMU_Center", self._sensors[self._sensor_names[12]],
                                           self._sensors[self._sensor_names[13]])

        self._imus["IMU_Center"] = imu_center

        # Pots
        self._sensors[self._sensor_names[14]] = Pot.Pot(self._sensor_names[14])
        self._sensors[self._sensor_names[15]] = Pot.Pot(self._sensor_names[15])
        self._sensors[self._sensor_names[16]] = Pot.Pot(self._sensor_names[16])
        self._sensors[self._sensor_names[17]] = Pot.Pot(self._sensor_names[17])
        self._sensors[self._sensor_names[18]] = Pot.Pot(self._sensor_names[18])
        self._sensors[self._sensor_names[19]] = Pot.Pot(self._sensor_names[19])

        # FSR
        self._sensors[self._sensor_names[20]] = FSR.FSR(self._sensor_names[20])
        self._sensors[self._sensor_names[21]] = FSR.FSR(self._sensor_names[21])
        self._sensors[self._sensor_names[22]] = FSR.FSR(self._sensor_names[22])
        self._sensors[self._sensor_names[23]] = FSR.FSR(self._sensor_names[23])
        self._sensors[self._sensor_names[24]] = FSR.FSR(self._sensor_names[24])
        self._sensors[self._sensor_names[25]] = FSR.FSR(self._sensor_names[25])

        self._sensor_manager.registar_all_sensors(self._sensors.values())

        for key, sensor in self._sensors.iteritems():
            print "sensor", sensor
            self._filter_manager.registar([BaseFilter.BaseFilter(sensor)], sensor)



    def __setup_robot(self):

        right_hip = Joint.Joint(self._imus["IMU_Right_Hip"], self._sensors["POT_Right_Hip"] )
        right_knee = Joint.Joint(self._imus["IMU_Right_Knee"], self._sensors["POT_Right_Knee"])
        fsr = [self._sensors["FSR_Right_01"], self._sensors["FSR_Right_02"], self._sensors["FSR_Right_03"]]
        right_ankle = Joint.Joint(self._imus["IMU_Right_Ankle"], self._sensors["POT_Right_Ankle"], fsr)
        self.right_leg = Leg.Leg(right_hip,right_knee,right_ankle)

        left_hip = Joint.Joint(self._imus["IMU_Left_Hip"], self._sensors["POT_Left_Hip"])
        left_knee = Joint.Joint(self._imus["IMU_Left_Knee"], self._sensors["POT_Left_Knee"])
        fsr = [self._sensors["FSR_Left_01"], self._sensors["FSR_Left_02"], self._sensors["FSR_Left_03"]]
        left_ankle = Joint.Joint(self._imus["IMU_Left_Ankle"], self._sensors["POT_Left_Ankle"], fsr)
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
