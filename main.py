from time import sleep

from interface.ui import UI as UI

img='splash.bmp'
print(f" - IMAGE: {img}")

display_ui = UI(splash_img=img)

display_ui.show_message()
for i in range(0,3):
    print(i+1)
    sleep(1)
display_ui.show_splash()
for i in range(0,3):
    print(i+1)
    sleep(1)


display_ui.clear_screen()
