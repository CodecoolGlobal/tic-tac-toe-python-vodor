import os
import time
import copy
# import pygame
import pyfiglet
import random
from colorama import Fore, Style  # Back


def init_board():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # row the outer, column the inner list(s)
    return board


def get_move(board, player):
    try:
        while True:
            move = input("Enter coordinates to mark or 'quit' to leave the game: ")
            if move == "quit" or move == "QUIT" or move == "Quit":
                clear()
                exit()
            elif len(move) == 1 or len(move) > 2 or move.isalpha():
                print_board(board)
                print("Enter a valid coordinate!")
            else:
                move = list(move)
                if move[1] not in "123":
                    print_board(board)
                    print("Enter a valid coordinate!")
                else:
                    row = move[0]
                    col = int(move[1])
                    if row not in "abcABC":
                        print_board(board)
                        print("Enter a valid coordinate!")
                    elif 0 > col or col > 4:
                        print_board(board)
                        print("Enter a valid coordinate!")
                    elif row in "aA":
                        row = 0
                        if board[row][col-1] != 0:
                            print_board(board)
                            print("This place is already taken, choose another coordinate!")
                        else:
                            col = (col - 1)
                            return row, col
                    elif row in "bB":
                        row = 1
                        if board[row][col-1] != 0:
                            print_board(board)
                            print("This place is already taken, choose another coordinate!")
                        else:
                            col = (col - 1)
                            return row, col
                    elif row in "cC":
                        row = 2
                        if board[row][col-1] != 0:
                            print_board(board)
                            print("This place is already taken, choose another coordinate!")
                        else:
                            col = (col - 1)
                            return row, col
    except KeyboardInterrupt:
        clear()
        print('Good bye!')
        exit()


def has_won(board, player):
    test_board = copy.deepcopy(board)
    wincondition = False
    for i in test_board:  # sor győzelem
        win_row = 0
        for k in i:
            if k == player:
                win_row += 1
            if win_row == 3:
                wincondition = True
    column_counter = 0
    while column_counter < 3:
        win_column = 0
        for i in test_board:
            if i[column_counter] == player:
                win_column += 1
            if win_column == 3:
                wincondition = True
        column_counter += 1
    if test_board[1][1] == player:
        if (test_board[0][0] == player) and (test_board[2][2] == player):
            wincondition = True
        if (test_board[2][0] == player) and (test_board[0][2] == player):
            wincondition = True
    return wincondition


def get_ai_move(board, player):
    time.sleep(1)
    ai_board = copy.deepcopy(board)
    row = 0
    for i in ai_board:  # tud-e győzni
        col = 0
        for z in i:
            if z == 0:
                i[col] = player
                if has_won(ai_board, player):
                    return row, col
                else:
                    i[col] = 0
            col += 1
        row += 1
    win_board = copy.deepcopy(board)
    if player == 1:
        player_win = 2
    elif player == 2:
        player_win = 1
    row = 0
    for i in win_board:  # tud-e az ellenfél győzni
        col = 0
        for z in i:
            if z == 0:
                i[col] = player_win
                if has_won(win_board, player_win):
                    return row, col
                else:
                    i[col] = 0
            col += 1
        row += 1

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if ai_board[row][col] == 0:
            return row, col


def get_ai_unbeatable_move(board, player):
    time.sleep(1)
    ai_board = copy.deepcopy(board)
    row = 0
    for i in ai_board:  # tud-e győzni
        col = 0
        for z in i:
            if z == 0:
                i[col] = player
                if has_won(ai_board, player):
                    return row, col
                else:
                    i[col] = 0
            col += 1
        row += 1

    win_board = copy.deepcopy(board)
    if player == 1:
        player_win = 2
    elif player == 2:
        player_win = 1
    row = 0
    for i in win_board:  # tud-e az ellenfél győzni
        col = 0
        for z in i:
            if z == 0:
                i[col] = player_win
                if has_won(win_board, player_win):
                    return row, col
                else:
                    i[col] = 0
            col += 1
        row += 1

    if (ai_board[0][0] == player_win) and ai_board[2][2] == 0:
        row = 2
        col = 2
        return row, col
    elif (ai_board[2][0] == player_win) and ai_board[0][2] == 0:
        row = 0
        col = 2
        return row, col
    elif (ai_board[0][2] == player_win) and ai_board[2][0] == 0:
        row = 2
        col = 0
        return row, col
    elif (ai_board[2][2] == player_win) and ai_board[0][0] == 0:
        row = 0
        col = 0
        return row, col
    # elif:
        # sarokba tenni először, ha nincs jobb opció

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if ai_board[row][col] == 0:
            return row, col


def mark(board, player, row, col):
    if (0 <= row) and (row <= 2) and (0 <= col) and (col <= 2):
        if board[row][col] == 0:
            board[row][col] = player
    return board


def is_full(board):
    k = 0
    for i in board:
        k += i.count(0)
    if k == 0:
        return True
    else:
        return False


def print_board(board):
    clear()
    play_board = []
    for i in board:
        for k in i:
            if k == 0:
                play_board.append('.')
            elif k == 1:
                play_board.append('X')
            else:
                play_board.append('O')
    print('')
    print('     1   2   3')
    print('')
    print('       |   |')
    print(' A   %s | %s | %s' % (play_board[0], play_board[1], play_board[2]))
    print('       |   |')
    print('   ----+---+----')
    print('       |   |')
    print(' B   %s | %s | %s' % (play_board[3], play_board[4], play_board[5]))
    print('       |   |')
    print('   ----+---+----')
    print('       |   |')
    print(' C   %s | %s | %s' % (play_board[6], play_board[7], play_board[8]))
    print('       |   |')
    return


def print_result(winner, player):
    win_char = 'O'
    if player == 1:
        win_char = 'X'
    if winner == 2:
        if win_char == 'O':
            ascii_banner = pyfiglet.figlet_format('The Winner Is :  O')
            print(Fore.YELLOW + ascii_banner)
            print(Style.RESET_ALL)
        else:
            ascii_banner = pyfiglet.figlet_format('The Winner Is :  X')
            print(Fore.YELLOW + ascii_banner)
            print(Style.RESET_ALL)
    elif winner == 1:
        ascii_banner = pyfiglet.figlet_format("It's a Tie!")
        print(Fore.RED + ascii_banner)
        print(Style.RESET_ALL)
    return


def player_select(player):
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    elif player == 0:
        player = 1
    else:
        print('Player error occured')
        time.sleep(5)
    return player


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    winner = 0
    player = 0  # player one(1) or two(2)
    full_board = False
    won = False
    if mode == 'HUMAN-HUMAN':
        player2 = 'human'
        player1 = 'human'
    elif mode == 'HUMAN-AI':
        player2 = 'ai'
        player1 = 'human'
    elif mode == 'AI-HUMAN':
        player1 = 'ai'
        player2 = 'human'
    elif mode == 'AI-AI':
        player1 = 'ai'
        player2 = 'ai'
    while True:
        clear()
        print_board(board)
        player = player_select(player)
        if (player == 2) and (player2 == 'human'):
            row, col = get_move(board, player)
        elif (player == 2) and (player2 == 'ai'):
            row, col = get_ai_move(board, player)
        elif (player == 1) and (player1 == 'human'):
            row, col = get_move(board, player)
        elif (player == 1) and (player1 == 'ai'):
            row, col = get_ai_move(board, player)
        mark(board, player, row, col)
        full_board = is_full(board)  # 0 - megy a játék, 1 - tie, 2 - győzelem
        won = has_won(board, player)
        if won:
            winner = 2
            break
        elif full_board:
            winner = 1
            break
    clear()
    print_board(board)
    print_result(winner, player)
    exit()


def clear():
    os.system('clear')
    return


def main_menu():
    # welcome_screen()
    while True:
        clear()
        print('Hi!\n\nDo you want to play?\n')
        print('1. Human vs Human\n2. Human vs A.I.\n3. A.I. vs Human\n4. A.I. vs A.I.\n5. Exit\n')
        begin = input('Choose(1-5):')
        if begin == '1':
            clear()
            tictactoe_game('HUMAN-HUMAN')
        elif begin == '2':
            clear()
            tictactoe_game('HUMAN-AI')
        elif begin == '3':
            clear()
            tictactoe_game('AI-HUMAN')
        elif begin == '4':
            tictactoe_game('AI-AI')
        elif begin == '5':
            exit()
    return


if __name__ == '__main__':
    main_menu()
