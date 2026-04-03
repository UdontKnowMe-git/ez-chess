import pyautogui
pyautogui.sleep(5)
# Adjust the confidence to 0.7 or 0.8 to account for the background
location = pyautogui.locateOnScreen('templates/white_pawn.png', confidence=0.7)

if location:
    print(f"I found the pawn's head at: {location}")
    pyautogui.moveTo(location)
else:
    print("Could not find it. Try a slightly larger crop (lower OFFSET).")