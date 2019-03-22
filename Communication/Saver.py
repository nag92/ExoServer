from Managers import SensorManager
import pickle

def watch(SM=SensorManager.SensorManager):

    while True:
        try:
            for key, sensor in SM.get_sensors().iteritems():
                print sensor.name, " ", sensor.type, " ", sensor.raw_values()
        except KeyboardInterrupt:
            print 'All done'
            # If you actually want the program to exit
            raise


def record(name, SM=SensorManager.SensorManager):

    with open(name + ".pkl", 'wb') as output:
        while True:
            try:
                pickle.dump(SM.get_sensors(), output)
            except KeyboardInterrupt:
                print 'All done'
                # If you actually want the program to exit
                raise


