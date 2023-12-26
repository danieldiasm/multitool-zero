from oled.SH1106 import SH1106

class UI(object):

    def __init__(self, display:SH1106, splash_img: str = None) -> None:
        self.display = display
        self.splash_img = splash_img

    def show_splash():
        pass

    def show_message():
        pass

    def show_menu():
        pass

class Menu(object):

    def __init__(self, type:str = "list", items:dict = {}) -> None:
        self.type = type
        self.items = items

