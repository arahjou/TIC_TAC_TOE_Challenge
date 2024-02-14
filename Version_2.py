import streamlit as st

# Initialize the game board
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
if 'turn' not in st.session_state:
    st.session_state.turn = 'X'
if 'winner' not in st.session_state:
    st.session_state.winner = None

# Function to check for a win or a tie
def check_winner():
    board = st.session_state.board
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return board[1][1]
    # Check for a tie
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        return 'Tie'
    return None

# Display the game board and handle player input
def display_board():
    winner = st.session_state.winner
    if winner:
        st.write(f'Winner: {winner}')
        if st.button('Play Again'):
            st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
            st.session_state.turn = 'X'
            st.session_state.winner = None
        return
    
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                if st.button(st.session_state.board[i][j] or ' ', key=f'button_{i}_{j}'):
                    if st.session_state.board[i][j] == '' and not winner:
                        st.session_state.board[i][j] = st.session_state.turn
                        st.session_state.turn = 'O' if st.session_state.turn == 'X' else 'X'
                        st.session_state.winner = check_winner()

display_board()
