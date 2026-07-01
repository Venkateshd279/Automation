import pyautogui 

import time 

# # mouse operation
# pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second

# # click the mouse at 100, 100
# pyautogui.click(100, 100)  # Click at (100, 100)
time.sleep(5)  # Wait for 5 seconds
# # right click the mouse at 100, 100
pyautogui.rightClick(300, 300)  # Right click at (300, 300)
# pyautogui.rightClick(100, 100)  # Right click at (100, 100)

# pyautogui.middleClick(100, 100)  # Middle click at (100, 100)
time.sleep(5)  # Wait for 5 seconds
pyautogui.scroll(+500)  # Scroll up 500 units
time.sleep(5)
pyautogui.scroll(-500)  # Scroll down 500 units

