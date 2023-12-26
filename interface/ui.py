from oled.SH1106 import SH1106
from PIL import Image,ImageDraw,ImageFont

class UI(object):

    def __init__(self, display:SH1106 = SH1106(), splash_img: str = None) -> None:
        def Initialize_Display():
            try:
                self.display.Init()
                self.display.clear()
                return True
            except Exception as e:
                return False
        
        self.display = display
        self.splash_img = splash_img
        if not Initialize_Display():
            raise RuntimeError("Failed to initialize display!")

    def show_splash(self):
        splash_image = Image.new('1', (self.display.width, self.display.height), 255)
        splash_bmp = ImageDraw.open(splash_image)
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

