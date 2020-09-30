import os


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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board, player, computer):
    print('\n' * 2)
    print(f'Player: {player}, Computer: {computer}')
    tmp = ["\n\033[4m  | A | B | C |"]
    tmp.append(f"1 | {board['A1']: <1} | {board['B1']: <1} | {board['C1']: <1} |")
    tmp.append(f"2 | {board['A2']: <1} | {board['B2']: <1} | {board['C2']: <1} |")
    tmp.append(f"3 | {board['A3']: <1} | {board['B3']: <1} | {board['C3']: <1} |")
    print('\n'.join(tmp))


print_board(BOARD, 'X', 'O')
