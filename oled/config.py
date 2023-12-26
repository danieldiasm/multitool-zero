# /*****************************************************************************
# * | File        :	  config.py
# * | Author      :   Waveshare team
# * | Function    :   Hardware underlying interface,for Jetson nano
# * | Info        :   Altered by Daniel Z D M (LeChevalier)
# *----------------
# * | Original version:   V1.0
# * | Date            :   2019-06-06
# * | Info            :   
# ******************************************************************************/
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import RPi.GPIO as GPIO
import time
from smbus import SMBus
import spidev

class Config(object):

    def __init__(self, Device_SPI:int = 1, Device_I2C:int = 0) -> None:
        # TODO Make the pins to be in a dictionary
        self.RST_PIN = 25
        self.DC_PIN  = 24
        self.CS_PIN  = 8
        self.BL_PIN  = 18
        # TODO Reduce those two variables to one
        self.Device_SPI = Device_SPI
        self.Device_I2C = Device_I2C

        if(self.Device_SPI == 1):
            self.Device = self.Device_SPI
            self.spi = spidev.SpiDev(0, 0)
        else :
            self.Device = self.Device_I2C
            self.address = 0x3C
            self.bus = SMBus(1)


    @staticmethod
    def digital_write(pin, value):
        GPIO.output(pin, value)


    @staticmethod
    def digital_read(pin):
        return GPIO.input(pin)


    def delay_ms(self,delaytime):
        time.sleep(delaytime / 1000.0)


    def spi_writebyte(self, data):
        self.spi.writebytes([data[0]])


    def i2c_writebyte(self, reg, value):
        self.bus.write_byte_data(self.address, reg, value)


    def module_init(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.RST_PIN, GPIO.OUT)
        GPIO.setup(self.DC_PIN, GPIO.OUT)
        GPIO.setup(self.CS_PIN, GPIO.OUT)
        GPIO.setup(self.BL_PIN, GPIO.OUT)

        if(self.Device == self.Device_SPI):
            self.spi.max_speed_hz = 10000000
            self.spi.mode = 0b00
        
        GPIO.output(self.CS_PIN, 0)
        GPIO.output(self.BL_PIN, 1)
        GPIO.output(self.DC_PIN, 0)
        return 0


    def module_exit(self):
        if(self.Device == self.Device_SPI):
            self.spi.SYSFS_software_spi_end()
        else :
            self.bus.close()
        GPIO.output(self.RST_PIN, 0)
        GPIO.output(self.DC_PIN, 0)
