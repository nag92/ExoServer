from Sensors import Accel, Gyro, Pot, FSR
from Managers import SensorManager, FilterManager
from Filters import BaseFilter
import rbdl


class Robot(object):

    def __init__(self, SM, ):
        self._sensor_names = []
        self._sensors = {}
        assert isinstance(SM, SensorManager.SensorManager)

        self._sensor_manager = SM
        self._filter_manager = FilterManager.FilterManager()
        self._filter_manager.register_observer(self._filter_manager)
        self.__setup_sensors()

    def __setup_sensors(self):
        self._sensor_names = ("IMU_Accel_Left_Foot",
                              "IMU_Gyro_Left_Foot",
                              "IMU_Accel_Right_Foot",
                              "IMU_Gyro_Right_Foot",
                              "IMU_Accel_Left_Knee",
                              "IMU_Gyro_Left_Knee",
                              "IMU_Accel_Right_Knee",
                              "IMU_Gyro_Right_Knee",
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

        # IMU Knee
        self._sensors[self._sensor_names[4]] = Accel.Accel(self._sensor_names[4])
        self._sensors[self._sensor_names[5]] = Gyro.Gyro(self._sensor_names[5])
        self._sensors[self._sensor_names[6]] = Accel.Accel(self._sensor_names[6])
        self._sensors[self._sensor_names[7]] = Gyro.Gyro(self._sensor_names[7])

        # IMU Center
        self._sensors[self._sensor_names[8]] = Accel.Accel(self._sensor_names[8])
        self._sensors[self._sensor_names[9]] = Gyro.Gyro(self._sensor_names[9])

        # Pots
        self._sensors[self._sensor_names[10]] = Pot.Pot(self._sensor_names[10])
        self._sensors[self._sensor_names[11]] = Pot.Pot(self._sensor_names[11])
        self._sensors[self._sensor_names[12]] = Pot.Pot(self._sensor_names[12])
        self._sensors[self._sensor_names[13]] = Pot.Pot(self._sensor_names[13])
        self._sensors[self._sensor_names[14]] = Pot.Pot(self._sensor_names[14])
        self._sensors[self._sensor_names[15]] = Pot.Pot(self._sensor_names[15])

        # FSR
        self._sensors[self._sensor_names[16]] = FSR.FSR(self._sensor_names[16])
        self._sensors[self._sensor_names[17]] = FSR.FSR(self._sensor_names[17])
        self._sensors[self._sensor_names[18]] = FSR.FSR(self._sensor_names[18])
        self._sensors[self._sensor_names[19]] = FSR.FSR(self._sensor_names[19])
        self._sensors[self._sensor_names[20]] = FSR.FSR(self._sensor_names[20])
        self._sensors[self._sensor_names[21]] = FSR.FSR(self._sensor_names[21])

        self._sensor_manager.registar_all_sensors(self._sensors)

        for sensor in self._sensors:
            self._filter_manager.registar(BaseFilter.BaseFilter(), sensor)

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
