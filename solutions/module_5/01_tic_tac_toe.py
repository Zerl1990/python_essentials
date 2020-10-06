import random


BOARD = {
    'A1': '',
    'A2': '',
    'A3': '',
    'B1': '',
    'B2': '',
    'B3': '',
    'C1': '',
    'C2': '',
    'C3': '',
}


def select_symbol():
    symbol = None
    while symbol not in ['X', 'O']:
        symbol = input('Select [X|O]:')
    return symbol


def print_board(board, player, computer):
    print('\n' * 2)
    print(f'Player: {player}, Computer: {computer}')
    tmp = ["\n\033[4m  | A | B | C |"]
    tmp.append(f"1 | {board['A1']: <1} | {board['B1']: <1} | {board['C1']: <1} |")
    tmp.append(f"2 | {board['A2']: <1} | {board['B2']: <1} | {board['C2']: <1} |")
    tmp.append(f"3 | {board['A3']: <1} | {board['B3']: <1} | {board['C3']: <1} |")
    print('\n'.join(tmp))


def player_move(board, symbol):
    valid_move = False
    while not valid_move:
        coordinate = input('Please select an empty cell:')
        valid_move = coordinate in board and not board[coordinate]
    board[coordinate] = symbol
    return check_winner(board, symbol)


def computer_move(board, symbol):
    keys = list(board.keys())
    random.shuffle(keys)
    for key in keys:
        if not board[key]:
            board[key] = symbol
            break
    return check_winner(board, symbol)


def check_winner(board, symbol):
    winner = __check_columns(board, symbol) or __check_rows(board, symbol)

    # First diagonal
    if board['A1'] == symbol and board['B2'] == symbol and board['C3'] == symbol:
        winner = True

    # Second diagonal
    if board['C1'] == symbol and board['B2'] == symbol and board['A3'] == symbol:
        winner = True

    if winner:
        print_board(board, player, computer)
        print(f'\n\n\tThe winner is {symbol}')
    return winner


def __check_columns(board, symbol):
    for column in ['A', 'B', 'C']:
        a1_cell = board[column + '1']
        a2_cell = board[column + '2']
        a3_cell = board[column + '3']
        if a1_cell == symbol and a2_cell == symbol and a3_cell == symbol:
            return True
    return False


def __check_rows(board, symbol):
    for row in ['1', '2', '3']:
        a_cell = board['A' + row]
        b_cell = board['B' + row]
        c_cell = board['C' + row]
        if a_cell == symbol and b_cell == symbol and c_cell == symbol:
            return True
    return False


def draw(board):
    empty_cells = [item for item in board.values() if not item]
    if len(empty_cells):
        return False
    else:
        print('~~~DRAW~~~')
        return True


player = select_symbol()
computer = 'O' if player == 'X' else 'X'
while True:
    print_board(BOARD, player, computer)
    if player_move(BOARD, player) or computer_move(BOARD, computer) or draw(BOARD):
        break
