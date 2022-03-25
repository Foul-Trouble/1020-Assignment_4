from board import *

def new_game():
    board = new_board()
    turn = "W"
    return board, turn


def print_game_state(b, turn):
    if turn == 'B':
        print("It is Black's turn")
    else:
        print("It is White's turn")
    pretty(b)