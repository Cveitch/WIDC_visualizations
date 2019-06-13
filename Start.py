# Author: Daniel O'Reilly

'''
The script should run as follows:
    -initial sleep for sensor warmup (no sensors require more than 5 seconds
    -configure all sensors with correct drivers and variables (sensorBase.sensorBase)
    -continuosly read data from the sensors (with a hour delay in between)
    -Once we receive the data, we upload the data directly to the database
        -this is done in the format
            -DateTime
            -Temperature 1 -> 8 if applicable (we will not have null of unneeded values, ie if there is no
            Temperature 8, this will not appear as Temperature8: null, or Temperature8: 999. Temperature 8
            will simply not appear. This is done was ease of the user, as well as easier querying
            -Humidity 1 -> 2. This follows the same protocal as above
            -Pressure 1. This follows the sampe protocal as above

        -Creating the system this way allows for easy implementation of future sensors.

    -It is the goal to create the system as plug and play as possible. At this point in the code,
    once all sensors have been decided and drivers written, the only area in the code a user would touch
    is to create a desired iD for the Pi. This is currently registered as an INT.


'''

import time
from SensorDriverPackage import sensorBase
import DataLogging.sensorLogging

time.sleep(5)

sensors = sensorBase.SensorBase()

while (1):
    data = sensors.readSensors()

    DataLogging.sensorLogging(3, data)

    time.sleep(3600)
    #enter time desired to read ever so often
