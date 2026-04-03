import pyautogui
import os

# Your verified "Perfect" values
START_X, START_Y = 246, 265
SQ = 80.75
OFFSET = 20  # This creates that 40x40 'head' shot you liked

# Create the folder if it doesn't exist
if not os.path.exists('templates'):
    os.makedirs('templates')

def save_piece(rank, file, name):
    # Calculate the top-left of the crop area
    left = START_X + (file * SQ) + OFFSET
    top = START_Y + (rank * SQ) + OFFSET
    
    # Take a 40x40 snippet
    img = pyautogui.screenshot(region=(int(left), int(top), 40, 40))
    img.save(f"templates/{name}.png")
    print(f"Captured: {name}.png")

# Mapping pieces to their starting squares
# Ranks: 0 (Black baseline), 1 (Black pawns), 6 (White pawns), 7 (White baseline)
piece_locations = {
    # Black Pieces
    (0, 0): "black_rook", (0, 1): "black_knight", (0, 2): "black_bishop",
    (0, 3): "black_queen", (0, 4): "black_king", (1, 0): "black_pawn",
    # White Pieces
    (7, 0): "white_rook", (7, 1): "white_knight", (7, 2): "white_bishop",
    (7, 3): "white_queen", (7, 4): "white_king", (6, 0): "white_pawn"
}

print("Starting capture in 5 seconds... Switch to the Chess.com tab!")
pyautogui.sleep(5)

for (r, f), name in piece_locations.items():
    save_piece(r, f, name)

print("\nAll templates saved to the 'templates' folder!")