import pyautogui
import pyperclip
import time

print("Make sure the AccuWeather page is open and visible in Chrome!")
print("Starting in 3 seconds...")
time.sleep(3)

# Click on the temperature
print("Clicking on temperature location (509, 180)...")
pyautogui.click(509, 180)
time.sleep(1)

# Triple-click to select the text
print("Selecting text...")
pyautogui.tripleClick(509, 180)
time.sleep(0.5)

# Copy
pyautogui.hotkey('command', 'c')
time.sleep(0.5)

# Read clipboard
temperature = pyperclip.paste()
print(f"\nCopied text: '{temperature}'")

if temperature:
    print("Success! Temperature copied.")
else:
    print("Nothing was copied. The coordinates may be off — try find_coordinates.py again.")
