import smbus2
import errno
import SensorDriverPackage.SHT31D
import SensorDriverPackage.BME280
import SensorDriverPackage.MCP9808


class SensorBase(object):

    def __init__(self):

        possibleTemperatureList = ['0x18', '0x19', '0x1A', '0x1B', '0x1C', '0x1D', '0x1E', '0x1F']
        possibleHumidityList = ['0x44', '0x45']
        possiblePressureList = ['0x78']

        self.temperatureSensorsUsed = []
        self.humiditySensorsUsed = []
        self.pressureSensorsUsed = []
        self.allSensorAddresses = []

        bus = smbus2.SMBus(1)
        amountOfDevices = 0

        for device in range(3, 128):
            try:
                bus.write_byte(device, 0)
                print("Found {0}".format(hex(device)))

                if hex(device) in possibleTemperatureList:
                    self.temperatureSensorsUsed.append(hex(device))
                    self.allSensorAddresses.append(device)


                elif hex(device) in possibleHumidityList:
                    self.humiditySensorsUsed.append(hex(device))
                    self.allSensorAddresses.append(device)

                elif hex(device) in possiblePressureList:
                    self.pressureSensorsUsed.append(hex(device))
                    self.allSensorAddresses.append(device)

                else:
                    print("Sensor Not Compatible with Current System")

                amountOfDevices += 1


            except IOError as e:
                if e.errno != errno.EREMOTE:
                    print("Error: {0} on address {1}".format(e, hex(device)))

            except Exception as e:
                print("Error: {0} on address {1}".format(e, hex(device)))

        for x in self.temperatureSensorsUsed:
            self.x = self.assignTemp(x)
            self.x.beginSensor()

        for x in self.humiditySensorsUsed:
            self.x = self.assignHumidity(x)

        for x in self.pressureSensorsUsed:
            self.x = self.assignPress(x)

    def readSensors(self):

        tempData = []
        for x in self.temperatureSensorsUsed:
            tempData.append(self.x.readTemperature())

        humidData = []
        for x in self.humiditySensorsUsed:
            humidData.append(self.x.readHumidity())

        pressureData = []
        for x in self.pressureSensorsUsed:
            pressureData.append(self.x.readHumidity())

            tempData = [1,2,3]
            humidData = [4,5,6]
            pressureData = [7,8,9]

        return tempData, humidData, pressureData

    def assignTemp(self, address):

        tempSensor = SensorDriverPackage.MCP9808.MCP9808(address)
        return tempSensor

    def assignHumidity(self, address):

        humidSensor = SensorDriverPackage.SHT31D.SHT31D(address)
        return humidSensor

    def assignPress(self, address):

        baroSensor = SensorDriverPackage.BME280.BME280(address)
        return baroSensor
