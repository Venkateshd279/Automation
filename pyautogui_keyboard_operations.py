import pyautogui
import time

pyautogui.typewrite("Hello, this is a test message!", interval=0.1)  # Type the message with a delay of 0.1 seconds between each character

# hot keys for mac
pyautogui.hotkey('command', 'space')  # Press Command + Space to open Spotlight search
pyautogui.hotkey('command', 'tab')  # Press Command + Tab to switch between applications
# pyautogui.hotkey('command', 'shift', '3')  # Press Command + Shift + 3 to take a screenshot
pyautogui.hotkey('command', 'a')  # Press Command + A to select all text


#special keys for mac
pyautogui.press('enter')  # Press the Enter key
pyautogui.press('backspace')  # Press the Backspace key
pyautogui.press('delete')  # Press the Delete key

#holding down a key
pyautogui.keyDown('shift')  # Hold down the Shift key
pyautogui.typewrite("this text is in uppercase")  # Type the message while holding down the Shift key
pyautogui.keyUp('shift')  # Release the Shift key

