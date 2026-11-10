import pyautogui
import keyboard
import time

switch = False

while True:
    if keyboard.is_pressed("q"):
     switch = not switch
     time.sleep(0.3)

    if switch:
     pyautogui.click()