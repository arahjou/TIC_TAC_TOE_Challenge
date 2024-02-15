import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the game variables
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
turn = 'X'
winner = None

# Function to draw the game board
def draw_board():
    window.fill(WHITE)
    # Draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(window, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    # Draw vertical lines
    for j in range(1, BOARD_COLS):
        pygame.draw.line(window, BLACK, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X or O on the board
def draw_moves():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(window, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), 
                                 ((col + 1) * SQUARE_SIZE - SQUARE_SIZE // 4, (row + 1) * SQUARE_SIZE - SQUARE_SIZE // 4), LINE_WIDTH)
                pygame.draw.line(window, RED, ((col + 1) * SQUARE_SIZE - SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE // 4, (row + 1) * SQUARE_SIZE - SQUARE_SIZE // 4), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 4, LINE_WIDTH)

# Function to check for a win or a tie
def check_winner():
    global winner
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != '':
            winner = board[row][0]
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != '':
            winner = board[0][col]
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        return True
    # Check for tie
    if all(board[row][col] != '' for row in range(BOARD_ROWS) for col in range(BOARD_COLS)):
        winner = 'Tie'
        return True
    return False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
            x, y = pygame.mouse.get_pos()
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            if board[row][col] == '':
                board[row][col] = turn
                turn = 'O' if turn == 'X' else 'X'
                if check_winner():
                    print(f"Winner: {winner}")
    
    draw_board()
    draw_moves()
    pygame.display.update()

pygame.quit()