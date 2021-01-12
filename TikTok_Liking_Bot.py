# Import relevant modules
import time
import pyautogui

# Give some time before python runs the rest of the code
time.sleep(5)

# Finding your mouse's current position on the screen
# print(pyautogui.position())

# The TikTok is located at x=550, y=520

pyautogui.moveTo(550, 520)
for i in range(5):
    time.sleep(0.5)
    pyautogui.doubleClick()
    time.sleep(0.5)
    pyautogui.scroll(-16)
