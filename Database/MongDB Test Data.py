from Database.MongoDB import sensorData


user = sensorData(
    piID = 1,
    temperature1 = 20,
    temperature2 = 40,
    temperature3 = 50,
    temperature4 = 60,
    temperature5 = 70,
    temperature6 = 80
).save()


user2 = sensorData(
    piID=2,
    temperature1=20,
    temperature2=40,
    temperature3=50,
    temperature4=60,
    temperature5=70,
    temperature6=80,
    temperature7 = 80,
    temperature8 = 90,
    pressure =10

).save()

'''

Currently we can upload data correctly to the database,
accepting values that are required (1-6 Temperature Readings)
with the ability to accept 7-8 Temperature, 1-2 Humidity, 
and 1 Pressure.

Future implementation of CO2 and particulate can easily be added


'''