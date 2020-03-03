import os
import time
# import pygame
import pyfiglet
# import random
from colorama import Fore, Style  # Back


def init_board():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # row the outer, column the inner list(s)
    return board


def taken(board, row, col):
    if board[row][col-1] != 0:
        print("This place is already taken, choose another coordinate!")
    else:
        return row, col


def get_move(board, player):
    move = input("Player %d enter coordinates to mark: " % (player))
    move = list(move)
    row = move[0]
    col = int(move[1])
    if len(move) > 2:
        print("Enter a valid coordinate!")
        move = list(move)
    elif row not in "abcABC":
        print("Enter a valid coordinate!")
    elif 0 > col or col > 4:
        print("Enter a valid coordinate!")
    elif row in "aA":
        row = 0
        taken(board, row, col)
        col = (col - 1)
        return(row, col)
    elif row in "bB":
        row = 1
        taken(board, row, col)
        col = (col - 1)
        return(row, col)
    elif row in "cC":
        row = 2
        taken(board, row, col)
        col = (col - 1)
        return(row, col)


def get_ai_move(board, player):
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    if (0 <= row) and (row <= 2) and (0 <= col) and (col <= 2):
        if board[row][col] == 0:
            board[row][col] = player
    return board


def has_won(board, player):
    wincondition = False
    for i in board:  # sor győzelem
        win_row = 0
        for k in i:
            if k == player:
                print(board)
            if win_row == 3:
                wincondition = True
    column_counter = 0
    while column_counter < 3:
        win_column = 0
        for i in board:
            if i[column_counter] == player:
                win_column += 1
            if win_column == 3:
                wincondition = True
            column_counter += 1
    if board[1][1] == player:
        if board[0][0] == player and board[2][2] == player:
            wincondition = True
        if board[2][0] == player and board[0][2] == player:
            wincondition = True
    return wincondition


def is_full(board):
    k = 0
    for i in board:
        k += i.count(0)
    if k == 0:
        return True
    else:
        return False


def print_board(board):
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
        ascii_banner = pyfiglet.figlet_format("The Winner Is ", win_char, '!')
        print(Fore.YELLOW + ascii_banner)
        print(Style.RESET_ALL)
    elif winner == 1:
        ascii_banner = pyfiglet.figlet_format("TIE")
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
    # welcome_screen()
    board = init_board()
    winner = 0
    player = 0  # player one(1) or two(2)
    full_board = False
    won = False
    while True:
        # AI esetén get_ai_move kell majd
        clear()
        print_board(board)
        player = player_select(player)
        row, col = get_move(board, player)
        mark(board, player, row, col)
        full_board = is_full(board)  # 0 - megy a játék, 1 - tie, 2 - győzelem
        won = has_won(board, player)
        print(full_board, won)
        if full_board:
            winner = 1
            break
        elif won:
            winner = 2
            break
    print_board(board)
    print_result(winner, player)


def clear():
    os.system('clear')
    return


def main_menu():
    tictactoe_game('HUMAN-HUMAN')
    return


if __name__ == '__main__':
    main_menu()
