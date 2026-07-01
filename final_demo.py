# I wants to take weather report from webpage and note on notepad 
# step 1 open my chrome browser on mac 

import pyautogui
import time
from datetime import datetime

# Enable failsafe - move mouse to top-left corner to abort script
pyautogui.FAILSAFE = True

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

# Copy URL to clipboard and paste (typewrite doesn't support special chars like :, /, .)
import subprocess
subprocess.run('pbcopy', input=weather_url.encode(), check=True)
pyautogui.hotkey('command', 'v')
time.sleep(1)

print("Pressing Enter to go to the webpage...")
pyautogui.press('enter')
time.sleep(5)
print("Webpage loaded successfully!")

# Step 3: Select all content on the webpage and copy it
print("Selecting all content on the webpage...")
pyautogui.hotkey('command', 'a')  # Select all content on the page
time.sleep(1)
pyautogui.hotkey('command', 'c')  # Copy the selected content
time.sleep(1)
print("Content copied successfully!")

# Step 4: Open TextEdit (Mac's Notepad equivalent) using Spotlight
print("Opening TextEdit...")
pyautogui.hotkey('command', 'space')  # Open Spotlight Search
time.sleep(2)

for char in 'TextEdit':
    pyautogui.prevss(char.lower())
    time.sleep(0.15)

time.sleep(1)
pyautogui.press('enter')  # Launch TextEdit
time.sleep(3)

# Open a new document in TextEdit
pyautogui.hotkey('command', 'n')
time.sleep(2)
print("TextEdit opened successfully with a new document!")

# Step 5: Paste the copied content into TextEdit
print("Pasting content into TextEdit...")
pyautogui.hotkey('command', 'v')  # Paste the copied content
time.sleep(2)
print("Content pasted successfully!")

# Step 6: Save the file with today's date as the filename
print("Saving the file...")
filename = "Weather_Chennai_" + datetime.today().strftime("%Y-%m-%d")
pyautogui.hotkey('command', 's')  # Open Save dialog
time.sleep(2)
pyautogui.hotkey('command', 'a')  # Select any existing filename text
time.sleep(0.5)
subprocess.run('pbcopy', input=filename.encode(), check=True)
pyautogui.hotkey('command', 'v')  # Paste the filename
time.sleep(0.5)
pyautogui.press('enter')  # Confirm save
time.sleep(2)
print(f"File saved as: {filename}")