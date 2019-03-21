from Sensors import Accel, Gyro, Pot, FSR
from Communication import Ethernet
from Managers import SensorManager


sensor_names = [ "IMU_Accel_Left_Foot",
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
                ]


sensors = []

#

# IMU Ankle
sensors.append(Accel.Accel("IMU_Accel_Left_Foot"))
sensors.append(Gyro.Gyro("IMU_Gyro_Left_Foot"))
sensors.append(Accel.Accel("IMU_Accel_Right_Foot"))
sensors.append(Gyro.Gyro("IMU_Gyro_Right_Foot"))

# IMU Knee
sensors.append(Accel.Accel("IMU_Accel_Left_Knee"))
sensors.append(Gyro.Gyro("IMU_Gyro_Left_Knee"))
sensors.append(Accel.Accel("IMU_Accel_Right_Knee"))
sensors.append(Gyro.Gyro("IMU_Gyro_Right_Knee"))

# IMU Center
sensors.append(Accel.Accel("IMU_Accel_Center"))
sensors.append(Gyro.Gyro("IMU_Gyro_Center"))

# Pots
sensors.append(Pot.Pot("POT_Left_Ankle"))
sensors.append(Pot.Pot("POT_Right_Ankle"))
sensors.append(Pot.Pot("POT_Left_Knee"))
sensors.append(Pot.Pot("POT_Right_Knee"))
sensors.append(Pot.Pot("POT_Left_Hip"))
sensors.append(Pot.Pot("POT_Right_Hip"))


#FSR
sensors.append(FSR.FSR("FSR_Right_01"))
sensors.append(FSR.FSR("FSR_Right_02"))
sensors.append(FSR.FSR("FSR_Right_03"))
sensors.append(FSR.FSR("FSR_Left_01"))
sensors.append(FSR.FSR("FSR_Left_02"))
sensors.append(FSR.FSR("FSR_Left_03"))

sensor_manager = SensorManager.SensorManager()
sensor_manager.registar_all_sensors(sensors)
COM = Ethernet.Ethernet()
COM.register_observer(sensor_manager)