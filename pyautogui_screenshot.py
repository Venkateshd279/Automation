import pyautogui
import time

import pyscreeze # pyscreeze is a dependency of pyautogui for taking screenshots

#take screenshot
screenshot = pyautogui.screenshot()  # Take a screenshot of the entire screen
screenshot.save("screenshot.png")  # Save the screenshot as "screenshot.png"