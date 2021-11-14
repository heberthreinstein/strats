import time
import vgamepad as vg

gamepad = vg.VX360Gamepad()

def pressButton(button):
    gamepad.press_button(button)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button)
    gamepad.update()
    time.sleep(0.1)

#Press a button to incialize emulator
pressButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
time.sleep(5)
#button to config
pressButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)