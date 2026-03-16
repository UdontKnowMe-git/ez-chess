import chess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize local board
board = chess.Board()
driver = webdriver.Chrome()  # Ensure you have the appropriate driver installed
driver.get("https://chess.com/")  

def get_last_move(driver):
    try:
        # Find all move elements
        moves = driver.find_elements(By.CSS_SELECTOR, "div.move .node")
        if moves:
            # The last element in the list is the most recent move
            return moves[-1].text 
    except:
        return None

# Logic Loop
last_scraped_move = ""
while not board.is_game_over():
    current_move_text = get_last_move(driver)
    
    if current_move_text and current_move_text != last_scraped_move:
        print(f"New move detected: {current_move_text}")
        board.push_san(current_move_text)
        last_scraped_move = current_move_text
        
        print(board)  # Print the current state of the board