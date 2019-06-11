import time
import datetime
from SensorDriverPackage import sensorBase
import Database
import DataLogging



time.sleep(1)

sensors = sensorBase.SensorBase()


while(1):

    data = sensors.readSensors()

    print(data)


