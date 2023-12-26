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
        print("DISPLAY READY")


    def show_splash(self):
        self.clear_screen()
        try:
            image = Image.new('1', (self.display.width, self.display.height), 255)
            splash_bmp = Image.open(self.splash_img)
            image.paste(splash_bmp, (0,5))
            self.display.ShowImage(self.display.getbuffer(image))
        except IOError as e:
            print(e)


    def show_message(self):
        image1 = Image.new('1', (self.display.width, self.display.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        font = ImageFont.truetype('Font.ttf', 20)
        font10 = ImageFont.truetype('Font.ttf',13)
        draw.text((30,0), 'Waveshare ', font = font10, fill = 0)
        draw.text((28,20), u'微雪电子 ', font = font, fill = 0)
        self.display.ShowImage(self.display.getbuffer(image1))

    def show_menu(self):
        pass


    def clear_screen(self):
        self.display.clear()


class Menu(object):

    def __init__(self, type:str = "list", items:dict = {}) -> None:
        self.type = type
        self.items = items

