import pyautogui
import time

print("Point to the Top-Left corner of the board in 3 seconds...")
time.sleep(3)
top_left = pyautogui.position()
print(f"Captured Top-Left: {top_left}")

print("Point to the Bottom-Right corner of the board in 3 seconds...")
time.sleep(3)
bottom_right = pyautogui.position()
print(f"Captured Bottom-Right: {bottom_right}")

board_width = bottom_right.x - top_left.x
square_size = board_width / 8
print(f"Square size is approximately: {square_size} pixels")