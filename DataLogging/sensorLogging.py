import time
import csv
import requests

from Database.MongoDB import sensorData

class sensorLogging(object):

    def sendDB(selfself, piid, datas):

        data = datas

        temperatureData = data[0]
        humidityData = data[1]
        pressureData = data[2]




        data = sensorData(

            piid = piid,

        )




