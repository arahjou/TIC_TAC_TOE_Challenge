import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets

# Initialize game board
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
if 'turn' not in st.session_state:
    st.session_state.turn = 'X'
if 'winner' not in st.session_state:
    st.session_state.winner = None

# Function to check for a win or a tie
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return board[1][1]
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        return 'Tie'
    return None

# Function to draw the Tic Tac Toe board with Matplotlib
def draw_board(board):
    fig, ax = plt.subplots(figsize=(5,5))
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    plt.xticks([])
    plt.yticks([])
    
    for i in range(1, 3):
        plt.plot([i, i], [0, 3], 'k-', linewidth=2)
        plt.plot([0, 3], [i, i], 'k-', linewidth=2)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                ax.text(j + 0.5, 2.5 - i + 0.5, 'X', fontsize=40, ha='center', va='center')
            elif board[i][j] == 'O':
                ax.text(j + 0.5, 2.5 - i + 0.5, 'O', fontsize=40, ha='center', va='center')
    
    return fig

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
    
    board = st.session_state.board
    fig = draw_board(board)
    st.pyplot(fig)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                button = widgets.Button(description='', layout=widgets.Layout(width='100px', height='100px'))
                button.on_click(lambda event, i=i, j=j: on_button_click(i, j))
                st.sidebar.write(button)

# Handler for button clicks
def on_button_click(i, j):
    if st.session_state.board[i][j] == '' and not st.session_state.winner:
        st.session_state.board[i][j] = st.session_state.turn
        st.session_state.turn = 'O' if st.session_state.turn == 'X' else 'X'
        st.session_state.winner = check_winner(st.session_state.board)

display_board()
