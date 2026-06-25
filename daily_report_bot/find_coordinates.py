import pyautogui
import time

print("You have 5 seconds to move your mouse over the temperature on the AccuWeather page...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

x, y = pyautogui.position()
print(f"\nYour mouse position is: X={x}, Y={y}")
print(f"Share these values with Claude!")
