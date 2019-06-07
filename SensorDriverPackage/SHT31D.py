import time
import smbus2


class SHT31D:

    def __init__(self, address):
        self.address = address
        self.bus = smbus2.SMBus(1)

    def readHumidity(self):
        self.bus.write_i2c_block_data(self.address,0x2C,[0x06])
        time.sleep(0.5)
        data = self.bus.read_i2c_block_data(self.address,0x00,6)
        return 100 * (data[3] * 256 + data[4]) / 65535

    def readTemperature(self):
        self.bus.write_i2c_block_data(self.address,0x2,[0x06])
        time.sleep(0.5)
        data = self.bus.read_i2c_block_data(self.address,0x00,6)
        rawTemp = data[0]*256 + data[1]
        return  -45 + (175 * rawTemp / 65535)





