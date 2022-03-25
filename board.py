def new_board():
    empty_board = [
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
    return empty_board


def colour(board, square):
    row_l, column_f = (val for val in square)
    row = (ord(row_l) - 96)
    column = (9 - int(column_f))
    callout = board[column][row]
    if 'Y' in callout:
        return 'B'
    elif 'X' in callout:
        return 'W'
    else:
        return None


def count_pieces(board, colour):
    if colour == 'B':
        c = 'Y'
    else:
        c = 'X'
    count = 0
    for i in board:
        for r in i:
            if c in r:
                count += 1
    return count


def piece(board, square):
    row_l, column_f = (val for val in square)
    row = (ord(row_l) - 96)
    column = (9 - int(column_f))
    callout = board[column][row]
    kind = callout.replace('X', "")
    kinds = kind.replace('Y', "")
    return kinds


def place_piece(board, square, colour, piece):
    row_l, column_f = (val for val in square)
    row = (ord(row_l) - 96)
    column = (9 - int(column_f))
    if colour == 'W':
        col = 'X'
    else:
        col = 'Y'
    name = piece + col

    board[column][row] = name


def pretty(board):
    view_board = []
    for i in board:
        r = []
        for n in i:
            m = n.replace("Y", "")
            o = m.replace("X", "")
            r.append(o)
        view_board.append(r)

    for i in view_board:
        print(' '.join(i))

