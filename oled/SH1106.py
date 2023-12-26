import oled.config as config
import RPi.GPIO as GPIO
import time
import numpy as np

Device_SPI = config.Device_SPI
Device_I2C = config.Device_I2C

LCD_WIDTH   = 128
LCD_HEIGHT  = 64

class SH1106(object):
    def __init__(self):
        self.width = LCD_WIDTH
        self.height = LCD_HEIGHT
        #Initialize DC RST pin
        self._dc = config.DC_PIN
        self._rst = config.RST_PIN
        self._bl = config.BL_PIN
        self.Device = config.Device
        self.disp_init_commands = [0xAE, 0x02, 0x10, 0x40, 0x81, 0xA0, 0xC0, 0xA6, 0xA8,
                                   0x3F, 0xD3, 0x00, 0xd5, 0x80, 0xD9, 0xF1, 0xDA, 0x12,
                                   0xDB, 0x40, 0x20, 0x02, 0xA4, 0xA6]


    """    Write register address and data     """
    def command(self, cmd):
        if(self.Device == Device_SPI):
            GPIO.output(self._dc, GPIO.LOW)
            config.spi_writebyte([cmd])
        else:
            config.i2c_writebyte(0x00, cmd)

    def Init(self):
        if (config.module_init() != 0):
            return False
            
        self.reset()
        
        for hex_cmd in self.disp_init_commands:
            self.command(hex_cmd)
            time.sleep(0.1)
        
        time.sleep(0.1)
        self.command(0xAF);
        
   
    def reset(self):
        """Reset the display"""
        GPIO.output(self._rst,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(self._rst,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self._rst,GPIO.HIGH)
        time.sleep(0.1)
    
    def getbuffer(self, image):
        buf = [0xFF] * ((self.width//8) * self.height)
        image_monocolor = image.convert('1')
        imwidth, imheight = image_monocolor.size
        pixels = image_monocolor.load()
        if(imwidth == self.width and imheight == self.height):
            for y in range(imheight):
                for x in range(imwidth):
                    if pixels[x, y] == 0:
                        buf[x + (y // 8) * self.width] &= ~(1 << (y % 8))
                        
        elif(imwidth == self.height and imheight == self.width):
            for y in range(imheight):
                for x in range(imwidth):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[(newx + (newy // 8 )*self.width) ] &= ~(1 << (y % 8))
        return buf
            
    def ShowImage(self, pBuf):
        for page in range(0,8):
            self.command(0xB0 + page);
            self.command(0x02); 
            self.command(0x10); 

            if(self.Device == Device_SPI):
                GPIO.output(self._dc, GPIO.HIGH);
            for i in range(0,self.width):
                if(self.Device == Device_SPI):
                    config.spi_writebyte([~pBuf[i+self.width*page]]); 
                else :
                    config.i2c_writebyte(0x40, ~pBuf[i+self.width*page])

    def clear(self):
        """Clear contents of image buffer"""
        _buffer = [0xff]*(self.width * self.height//8)
        self.ShowImage(_buffer) 
    