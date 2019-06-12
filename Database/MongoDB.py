# Author: Daniel O'Reilly

from mongoengine import *
from datetime import datetime
import json

# Connected to MONGODB with basic authentification
'''
connect(db = "widc_DB",
        username = "root",
        password = "WIDC123!",
        authentication_source = "admin",
        host = "localhost",
        port = 27017
        )
'''

# This connect is used for easer testing
connect("WIDC")


# Basic Creation of Desired Values
class sensorData(Document):
    piID = IntField(required=False)
    dateSent = DateTimeField(default=datetime.utcnow)
    temperature1 = IntField(required=False )
    temperature2 = IntField(required=False )
    temperature3 = IntField(required=False)
    temperature4 = IntField(required=False)
    temperature5 = IntField(required=False)
    temperature6 = IntField(required=False)
    temperature7 = IntField(required=False)
    temperature8 = IntField(required=False)
    humidity1 = IntField(required=False)
    humidity2 = IntField(required=False)
    pressure = IntField(required=False)

    # carbonRead = IntField(required = False)
    # particulate = IntField(required = False)

    # Basic Return of Desired Values
    def jsonReturn(self):
        sensor_Dict = {

            "piID": self.piID,
            "dateSent": self.dateSent,
            "temperature1": self.temperature1,
            "temperature2": self.temperature2,
            "temperature3": self.temperature3,
            "temperature4": self.temperature4,
            "temperature5": self.temperature5,
            "temperature6": self.temperature6,
            "temperature7": self.temperature7,
            "temperature8": self.temperature8,
            "humidity1": self.humidity1,
            "humidity2": self.humidity2,
            "pressure": self.pressure
            # "carbonRead": self.carbonRead
            # "particulate": self.particulate

        }
        return json.dumps(sensor_Dict)

    meta = {

        "indexes": ["piID", "dateSent"],
        "ordering": ["-dateSent"]

    }
