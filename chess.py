from board import *


def new_game():
    board = [
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '],
        ['8', 'RY', 'NY', 'BY', 'QY', 'KY', 'BY', 'NY', 'RY', '8'],
        ['7', 'PY', 'PY', 'PY', 'PY', 'PY', 'PY', 'PY', 'PY', '7'],
        ['6', '□', '□', '□', '□', '□', '□', '□', '□', '6'],
        ['5', '□', '□', '□', '□', '□', '□', '□', '□', '5'],
        ['4', '□', '□', '□', '□', '□', '□', '□', '□', '4'],
        ['3', '□', '□', '□', '□', '□', '□', '□', '□', '3'],
        ['2', 'PX', 'PX', 'PX', 'PX', 'PX', 'PX', 'PX', 'PX', '2'],
        ['1', 'RX', 'NX', 'BX', 'QX', 'KX', 'BX', 'NX', 'RX', '1'],
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' ']
    ]
    turn = "W"
    return board, turn


def print_game_state(b, turn):
    if turn == 'B':
        print("It is Black's turn")
    else:
        print("It is White's turn")
    pretty(b)


