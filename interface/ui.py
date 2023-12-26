from oled.SH1106 import SH1106
from PIL import Image,ImageDraw,ImageFont

class UI(object):

    def __init__(self, splash_img: str = None) -> None:
        def Initialize_Display():
            try:
                self.display.Init()
            except Exception as e:
                raise Exception(e)
            self.display.clear()
   
        self.display = SH1106()
        self.splash_img = splash_img
        Initialize_Display()


    def show_splash(self):
        splash_image = Image.new('1', (self.display.width, self.display.height), 255)
        splash_bmp = Image.open(self.splash_img)
        splash_image.paste(splash_bmp, (0,5))
        self.display.ShowImage(self.display.getbuffer(splash_bmp))


    def show_message(self):
        pass


    def show_menu(self):
        pass


    def clear_screen(self):
        self.display.clear()


class Menu(object):

    def __init__(self, type:str = "list", items:dict = {}) -> None:
        self.type = type
        self.items = items

