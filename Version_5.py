import streamlit as st
import random

# Initialize the board and turn if not already done
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
if 'turn' not in st.session_state:
    st.session_state.turn = 'X'

# Custom CSS to make buttons closer like a calculator
st.markdown(
    """
    <style>
    .css-18e3th9 {
        padding: 0px !important;
        margin: 0px !important;
    }
    .stButton>button {
        width: 100%;
        height: 3em;  # Adjust the height if needed
        margin: 3px 0;  # Small margin between buttons
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def check_winner(board):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return ''

def check_draw(board):
    for row in board:
        if '' in row:
            return False
    return True

def make_computer_move():
    empty_positions = [(i, j) for i in range(3) for j in range(3) if st.session_state.board[i][j] == '']
    if empty_positions:
        i, j = random.choice(empty_positions)
        st.session_state.board[i][j] = 'O'

def restart_game():
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.turn = 'X'

def display_winner_or_draw():
    winner = check_winner(st.session_state.board)
    if winner:
        st.write(f'Player {winner} wins!')
        return True
    elif check_draw(st.session_state.board):
        st.write('Draw!')
        return True
    return False

def tic_tac_toe_board():
    # Display the board with buttons
    for i in range(3):
        cols = st.columns(3, gap="small")
        for j, col in enumerate(cols):
            with col:
                if st.session_state.board[i][j] == '':
                    if st.button(' ', key=f'button_{i}_{j}'):
                        st.session_state.board[i][j] = st.session_state.turn
                        st.session_state.turn = 'O'
                        if display_winner_or_draw():
                            restart_game()
                            return
                        make_computer_move()
                        st.session_state.turn = 'X'
                        if display_winner_or_draw():
                            restart_game()
                            return
                else:
                    st.button(st.session_state.board[i][j], key=f'button_{i}_{j}', disabled=True)

# Display the Tic Tac Toe board and the restart button
tic_tac_toe_board()

if st.button('Restart Game'):
    restart_game()
