from time import sleep

from interface.ui import UI as UI

display_ui = UI(splash_img="splash.bmp")

display_ui.show_splash()
for i in range(0,10):
    print(i+1)
    sleep(1)

display_ui.clear_screen()
