import smbus2
import bme280


class BME280:

    def __init__(self,address):

        port = 1
        address = address
        bus = smbus2.SMBus(port)
        calibrate = bme280.load_calibration_params(bus, address)
        self.data = bme280.sample(bus, address, calibrate)

    def readTemperature(self):
       return self.data.temperature

    def readHumidity(self):
        return self.data.humidity

    def readPressure(self):
        return self.data.pressure