import keyboard
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

#Constants
ERS_CHARGING = 1
ERS_BALANCED_LOW = 2
ERS_BALANCED_HIGH = 3
ERS_OVERTAKE = 4
ERS_TOP_SPEED = 5
ERS_HOTLAP = 6

MGU_H_BATERY = 1
MGU_H_MOTOR = 2

#Buttons
BTN_DELIV_INC = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
BTN_DELIV_DEC = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
BTN_RECOV_INC = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
BTN_RECOV_DEC = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
BTN_MGU_H = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
BTN_EB_INC = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
BTN_EB_DEC = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
BTN_BB_FWRD = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
BTN_BB_REAR = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB


#SETUP
SETUP_ERS_MODE = ERS_CHARGING
SETUP_ERS_RECOVERY = 9
SETUP_ENGINE_BRAKE = 8
SETUP_MGUH = MGU_H_BATERY
SETUP_BREAK_BALANCE = 53

#GLOBALS
currentERSMode = SETUP_ERS_MODE
currentERSRecovery = SETUP_ERS_RECOVERY
currentEngineBraking = SETUP_ENGINE_BRAKE
currentMGUH = SETUP_MGUH
currentBreakBalance = SETUP_BREAK_BALANCE

def reset():
    global currentERSMode
    currentERSMode = SETUP_ERS_MODE
    global currentERSRecovery
    currentERSRecovery = SETUP_ERS_RECOVERY
    global currentEngineBraking
    currentEngineBraking = SETUP_ENGINE_BRAKE
    global currentMGUH
    currentMGUH = SETUP_MGUH
    global currentBreakBalance
    currentBreakBalance = SETUP_BREAK_BALANCE
    print('RESET')

def changeERSMode(mode):
    print("Changing ERS =>", mode)
    global currentERSMode
    diff = mode - currentERSMode
    if (diff > 0): 
        for _ in range(diff):
            pressButton(BTN_DELIV_INC)
        currentERSMode = mode

    if (diff < 0):
        for _ in range(abs(diff)): 
            pressButton(BTN_DELIV_DEC)
        currentERSMode = mode

def changeRecovery(n):
    print("Changing Recovery =>", n)
    global currentERSRecovery
    diff = n - currentERSRecovery
    if (diff > 0): 
        for _ in range(diff):
            pressButton(BTN_RECOV_INC)
        currentERSRecovery = n

    if (diff < 0):
        for _ in range(abs(diff)): 
            pressButton(BTN_RECOV_DEC)
        currentERSRecovery = n

def changeEngineBraking(n):
    print("Changing Engine Brake =>", n)
    global currentEngineBraking
    diff = n - currentEngineBraking
    if (diff > 0): 
        for _ in range(diff):
            pressButton(BTN_EB_INC)
        currentEngineBraking = n

    if (diff < 0):
        for _ in range(abs(diff)): 
            pressButton(BTN_EB_DEC)
        currentEngineBraking = n

def changeBreakBalance(n):
    print("Changing Break Balance =>", n)
    global currentBreakBalance
    diff = n - currentBreakBalance
    if (diff > 0): 
        for _ in range(diff):
            pressButton(BTN_BB_FWRD)
            pressButton(BTN_BB_FWRD)
        currentBreakBalance = n

    if (diff < 0):
        for _ in range(abs(diff)): 
            pressButton(BTN_BB_REAR)
            pressButton(BTN_BB_REAR)
        currentBreakBalance = n

def changeMGUH(mode):
    print("Changing MGUH =>", mode)
    global currentMGUH
    if(mode != currentMGUH):
        pressButton(BTN_MGU_H)
        currentMGUH = mode

def recharge():
    changeERSMode(ERS_CHARGING)
    changeRecovery(10)
    changeEngineBraking(11)
    changeMGUH(MGU_H_BATERY)

def setup():
    changeERSMode(SETUP_ERS_MODE)
    changeRecovery(SETUP_ERS_RECOVERY)
    changeEngineBraking(SETUP_ENGINE_BRAKE)
    changeMGUH(SETUP_MGUH)

def qualifying():
    changeERSMode(ERS_HOTLAP)
    changeMGUH(MGU_H_MOTOR)
    changeRecovery(0)
    changeEngineBraking(SETUP_ENGINE_BRAKE)

def stratOne():
    changeEngineBraking(11)
    changeBreakBalance(53)

def stratTwo():
    changeEngineBraking(8)
    changeBreakBalance(55)

def push():
    changeRecovery(4)
    changeERSMode(ERS_BALANCED_HIGH)

def saveBattery():
    changeERSMode(ERS_BALANCED_LOW)
    changeRecovery(10)
    changeEngineBraking(10)
    changeBreakBalance(57)
    changeMGUH(MGU_H_BATERY)

def fullPush():
    changeERSMode(ERS_OVERTAKE)
    changeRecovery(4)
    changeMGUH(MGU_H_MOTOR)

def sendIT():
    changeERSMode(ERS_TOP_SPEED)
    changeEngineBraking(SETUP_ENGINE_BRAKE)
    changeMGUH(MGU_H_MOTOR)
    changeRecovery(0)


while True:
    keyboard.add_hotkey('r', recharge)
    keyboard.add_hotkey('c', fullPush)
    keyboard.add_hotkey('v', changeERSMode, [ERS_BALANCED_HIGH])
    keyboard.add_hotkey('z', push)
    keyboard.add_hotkey('x', saveBattery)
    keyboard.add_hotkey('q', qualifying)
    keyboard.add_hotkey('s', setup)
    keyboard.add_hotkey('1', stratOne)
    keyboard.add_hotkey('2', stratTwo)
    keyboard.add_hotkey('0', reset)

    keyboard.wait()