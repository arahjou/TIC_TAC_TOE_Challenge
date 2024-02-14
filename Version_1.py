import numpy as np

# creating first function
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " " or board[2][0] == board[1][1] == board[0][2] != " ":
        return board[1][1]
    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("This position is already taken.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_player_move(current_player, board)
        board[row][col] = current_player

        winner = check_win(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    if input("Play again? (y/n): ").lower().startswith('y'):
        play_game()

if __name__ == "__main__":
    play_game()
