# Author - Daniel O'Reilly

from Database.MongoDB import sensorData


class sensorLogging(object):

    def sendDB(selfself, piid, data):

        form = data

        temperatureData = form[0]
        humidityData = form[1]
        pressureData = form[2]

        form = sensorData()

        try:

            form.temperature1 = temperatureData[0]
            form.save()

        except IndexError:

            form.temperature1 = 'null'

        try:

            form.temperature2 = temperatureData[1]
            form.save

        except IndexError:

            form.temperature2 = 'null'

        try:

            form.temperature3 = temperatureData[2]
            form.save()

        except IndexError:

            form.temperature3 = 'null'

        try:

            form.temperature4 = temperatureData[3]
            form.save()


        except IndexError:

            form.temperature4 = 'null'

        try:

            form.temperatre5 = temperatureData[4]
            form.save

        except IndexError:

            form.temperature5 = 'null'

        try:

            form.temperature6 = temperatureData[5]
            form.save()


        except IndexError:

            form.temperature6 = 'null'

        try:

            form.temperature7 = temperatureData[6]
            form.save


        except IndexError:

            form.temperature7 = 'null'

        try:

            form.temperature8 = temperatureData[7]
            form.save()

        except IndexError:

            form.temperature8 = 'null'

        try:

            form.humidity1 = humidityData[0]
            form.save()

        except IndexError:

            form.humidity1 = 'null'

        try:

            form.humimidity2 = humidityData[1]
            form.save()


        except IndexError:

            form.humidity2 = humidityData[2]

        try:

            form.pressure = pressureData[0]
            form.save()

        except IndexError:

            form.pressure = 'null'
