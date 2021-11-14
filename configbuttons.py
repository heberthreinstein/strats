import time
import vgamepad as vg

BTN_DELIV_INC = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
BTN_DELIV_DEC = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
BTN_RECOV_INC = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
BTN_RECOV_DEC = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
BTN_MGU_H = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
BTN_EB_INC = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
BTN_EB_DEC = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
BTN_BB_FWRD = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
BTN_BB_REAR = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB

gamepad = vg.VX360Gamepad()

def pressButton(button):
    gamepad.press_button(button)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button)
    gamepad.update()
    time.sleep(0.1)

pressButton(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

countToTen():
    for i in range(10): 
        print(i)
        time.sleep(1)

print("Delivery increse button will be pressed in 10seconds")
countToTen()
pressButton(BTN_DELIV_INC)
print("Delivery decrease button will be pressed in 10seconds")
countToTen()
pressButton(BTN_DELIV_DEC)
print("Recovery increse button will be pressed in 10seconds")
countToTen()
pressButton(BTN_RECOV_INC)
print("Recovery decrease button will be pressed in 10seconds")
countToTen()
pressButton(BTN_RECOV_DEC)
print("MGU H button will be pressed in 10seconds")
countToTen()
pressButton(BTN_MGU_H)
print("Engine Brake increse button will be pressed in 10seconds")
countToTen()
pressButton(BTN_EB_INC)
print("Engine Brake decrease button will be pressed in 10seconds")
countToTen()
pressButton(BTN_EB_DEC)
print("Break bias foward button will be pressed in 10seconds")
countToTen()
pressButton(BTN_BB_FWRD)
print("Break bias backword button will be pressed in 10seconds")
countToTen()
pressButton(BTN_BB_REAR)
