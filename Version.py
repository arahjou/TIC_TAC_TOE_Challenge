import random

# Constants for player symbols and empty cell
X = "X"
O = "O"
EMPTY = "-"

# Winning combinations on the Tic Tac Toe board
WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
    (0, 4, 8), (2, 4, 6)               # Diagonal
]

# Function to print the game board
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

# Function for player input
def player_input(board):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if 1 <= inp <= 9 and board[inp-1] == EMPTY:
                return inp - 1
            else:
                print("Invalid input or position already taken. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to check if a player has won
def check_win(board):
    for combination in WINNING_COMBINATIONS:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != EMPTY:
            return True
    return False

# Function to check if the game is a tie
def check_tie(board):
    return EMPTY not in board

# Function for computer's move
def computer_move(board):
    position = random.randint(0, 8)
    while board[position] != EMPTY:
        position = random.randint(0, 8)
    board[position] = O

# Function to switch player turns
def switch_player(current_player):
    return X if current_player == O else O

# Main function to run the game
def main():
    board = [EMPTY] * 9
    current_player = X

    while True:
        print_board(board)

        if current_player == X:
            position = player_input(board)
            board[position] = X
        else:
            computer_move(board)

        if check_win(board):
            print_board(board)
            print(f"The winner is {current_player}!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = switch_player(current_player)

# Entry point of the program
if __name__ == "__main__":
    main()
