import Adafruit_MCP9808.MCP9808 as MCP9808

class MCP9808:

    def __init__(self, address):

        self.sensor = MCP9808.MCP9808(address)

    def beginSensor(self):
        self.sensor.begin()

    def readTemp(self):
        return self.sensor.readTempC()



