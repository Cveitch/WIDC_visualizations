from mongoengine import *
from datetime import datetime
import json




#Connected to MONGODB with basic authentification

connect(db = "widc_DB",
        username = "root",
        password = "WIDC123!",
        authentication_source = "admin",
        host = "localhost",
        port = 27017
        )


#Basic Creation of Desired Values
class sensorData(Document):
    piID = IntField(required = True)
    dateSent = DateTimeField(default= datetime.utcnow)
    temperature1 = IntField(required = True