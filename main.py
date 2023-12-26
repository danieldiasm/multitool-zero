from time import sleep

from interface.ui import UI as UI

display_ui = UI(splash_img="splash.bmp")

display_ui.show_splash()
sleep(10)
display_ui.clear_screen()
