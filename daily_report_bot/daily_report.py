import pyautogui
import time
import subprocess
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

# Give time to switch focus away from terminal before automation starts
print("Starting in 5 seconds... click on your Desktop or any other app now!")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

# Click on desktop to make sure terminal loses focus
pyautogui.click(100, 100)
time.sleep(1)

# Step 1: Open Chrome browser on Mac using pyautogui
print("Opening Spotlight Search...")
pyautogui.hotkey('command', 'space')  # Press Command + Space to open Spotlight search
time.sleep(2)  # Increased wait time for Spotlight to fully appear

print("Typing Chrome...")
# Type 'Chrome' with longer interval for reliability
for char in 'Chrome':
    pyautogui.press(char.lower())
    time.sleep(0.15)

time.sleep(1)
print("Pressing Enter to launch Chrome...")
pyautogui.press('enter')  # Press Enter to open Chrome
time.sleep(4)  # Wait for Chrome to fully load

print("Chrome opened successfully!")

# Step 2: Navigate to the weather report webpage
print("Navigating to the weather report webpage...")
weather_url = "https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671?type=locality&city=chennai"

# Open a new tab and focus the address bar
pyautogui.hotkey('command', 't')
time.sleep(1)

# Type the URL character by character
pyautogui.write(weather_url, interval=0.03)
time.sleep(1)

print("Pressing Enter to go to the webpage...")
pyautogui.press('enter')
time.sleep(5)
print("Webpage loaded successfully!")

# Step 3: Right-click on the temperature and copy it
print("Right-clicking on temperature to copy...")
pyautogui.rightClick(509, 180)
time.sleep(1)

# Click 'Copy' from the context menu
pyautogui.hotkey('command', 'c')
time.sleep(0.5)

# Read the copied temperature from clipboard
import pyperclip
temperature = pyperclip.paste()
print(f"Temperature copied: {temperature}")

# Step 4: Open Numbers using Spotlight
print("Opening Numbers...")
pyautogui.hotkey('command', 'space')
time.sleep(2)

for char in 'Numbers':
    pyautogui.press(char.lower())
    time.sleep(0.15)

time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

# Open a new spreadsheet from template chooser
pyautogui.hotkey('command', 'n')
time.sleep(3)

# Press Enter to select the default Blank template
pyautogui.press('enter')
time.sleep(3)
print("Numbers opened with a new spreadsheet!")

# Maximize Numbers window to fullscreen so coordinates are always consistent
pyautogui.hotkey('command', 'ctrl', 'f')
time.sleep(2)
print("Numbers maximized to fullscreen!")

time.sleep(2)
# Click on cell A1 directly using fullscreen coordinates
pyautogui.click(92, 202)
time.sleep(0.5)


# Step 5: Add headers and data into Numbers
print("Adding headers and data into Numbers...")

today_date = datetime.today().strftime("%Y-%m-%d")
today_time = datetime.today().strftime("%H:%M:%S")
# temperature = "N/A"  # placeholder - will be fetched from website in full script



# A1 - Header: Date
pyautogui.write('Date', interval=0.05)
time.sleep(0.3)

# move to B1 cell 
pyautogui.press('tab')
time.sleep(0.3)

# subprocess.run('pbcopy', input='Date'.encode(), check=True)
# pyautogui.hotkey('command', 'v')
# time.sleep(0.3)
# pyautogui.press('tab')
# time.sleep(0.3)

# B1 - Header: Time
subprocess.run('pbcopy', input='Time'.encode(), check=True)
pyautogui.hotkey('command', 'v')
time.sleep(0.3)
pyautogui.press('tab')
time.sleep(0.3)

# C1 - Header: Short Notes
subprocess.run('pbcopy', input='Short Notes'.encode(), check=True)
pyautogui.hotkey('command', 'v')
time.sleep(0.3)
pyautogui.press('return')
time.sleep(0.3)

# After tabbing A1->B1->C1 and pressing Return, cursor moves to A2
# A2 - Today's date
subprocess.run('pbcopy', input=today_date.encode(), check=True)
pyautogui.hotkey('command', 'v')
time.sleep(0.3)
pyautogui.press('tab')
time.sleep(0.3)

# B2 - Today's time
subprocess.run('pbcopy', input=today_time.encode(), check=True)
pyautogui.hotkey('command', 'v')
time.sleep(0.3)
pyautogui.press('tab')
time.sleep(0.3)

# C2 - Copied temperature from website
subprocess.run('pbcopy', input=temperature.encode(), check=True)
pyautogui.hotkey('command', 'v')
time.sleep(1)
print("Data entered into Numbers successfully!")

# Step 6: Save the file as daily_report_yyyy_mm_dd.numbers
print("Saving the file...")
filename = f"daily_report_{today_date}"

pyautogui.hotkey('command', 's')
time.sleep(2)

# Clear existing name and type new filename
pyautogui.hotkey('command', 'a')
time.sleep(0.3)
subprocess.run('pbcopy', input=filename.encode(), check=True)
pyautogui.hotkey('command', 'v')
time.sleep(0.5)
pyautogui.press('return')
time.sleep(2)
print(f"File saved as: {filename}.numbers")

# Step 7: Take a screenshot and save with same date format
print("Taking screenshot...")
screenshot_filename = f"daily_report_{today_date}.png"
pyautogui.screenshot(screenshot_filename)
print(f"Screenshot saved as: {screenshot_filename}")

# -- TextEdit steps (commented out for future use) --
# Step 4: Open TextEdit using Spotlight
# print("Opening TextEdit...")
# pyautogui.hotkey('command', 'space')
# time.sleep(2)
#
# for char in 'TextEdit':
#     pyautogui.press(char.lower())
#     time.sleep(0.15)
#
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(3)
#
# # Open a new document
# pyautogui.hotkey('command', 'n')
# time.sleep(2)
# print("TextEdit opened with a new document!")
#
# # Step 5: Paste the temperature into TextEdit
# print("Pasting temperature into TextEdit...")
# pyautogui.hotkey('command', 'v')
# time.sleep(1)
# print("Temperature pasted successfully!")
