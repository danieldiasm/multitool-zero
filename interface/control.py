
import RPi.GPIO as GPIO

class Buttons(object):

    def __init__(self) -> None:

        def control_hw_setup():
            GPIO.setmode(GPIO.BCM)
            for key, value in self.keymap.items():
                GPIO.setup(value, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # TODO Make this keymap come from an INI file
        self.keymap = {
            "KEY_UP_PIN": 6 ,
            "KEY_DOWN_PIN": 19,
            "KEY_LEFT_PIN": 5,
            "KEY_RIGHT_PIN": 26,
            "KEY_CENTER_PIN": 13,
            "KEY1_PIN": 21,
            "KEY2_PIN": 20,
            "KEY3_PIN": 16,
        }
        control_hw_setup()

    def key_press(self, key):
        GPIO.input(key)
    
    def key_up(self):
        self.key_press(self.keymap["KEY_UP_PIN"])

    def key_down(self):
        self.key_press(self.keymap["KEY_DOWN_PIN"])
            
    def key_left(self):
        self.key_press(self.keymap["KEY_LEFT_PIN"])

    def key_right(self):
        self.key_press(self.keymap["KEY_RIGHT_PIN"])

    def key_center(self):
        self.key_press(self.keymap["KEY_CENTER_PIN"])

    def key_1(self):
        self.key_press(self.keymap["KEY1_PIN"])

    def key_2(self):
        self.key_press(self.keymap["KEY2_PIN"])

    def key_3(self):
        self.key_press(self.keymap["KEY3_PIN"])
