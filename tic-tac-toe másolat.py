# import os
# import time
# import pygame
# import random


def init_board():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # row the outer, column the inner list(s)
    return board


def get_move(board, player):
    move = input("Enter coordinates to mark: ")
    move = list(move)
    row = move[0]
    col = move[1]
    if len(move) > 2:
        print("Enter a valid coordinate!")
        move = list(move)
    elif row not in "abcABC":
        print("Enter a valid coordinate!")
    elif 0 > int(col) or int(col) > 4: 
        print("Enter a valid coordinate!")
    elif row in "aA":
        row = 0
        if board[row][int(col)-1] != 0:
            print("This place is already taken, choose another coordinate!")
        else:
            return(row,col)
    elif row in "bB":
        row = 1
        if board[row][int(col)-1] != 0:
            print("This place is already taken, choose another coordinate!")
        else:
            return(row,col)
    elif row in "cC":
        row = 2
        if board[row][int(col)-1] != 0:
            print("This place is already taken, choose another coordinate!")
        else:
            return(row,col)

def get_ai_move(board, player):
    row, col = 0, 0
    return row, col
    pass


def mark(board, player, row, col):
    if (0 <= row < 2) and (0 <= col < 2):
        if board[row][col] == 0:
            board[row][col] = player
    return board


def has_won(board, player):
    return False


def is_full(board):
    k = 0
    for i in board:
        k += i.count(0)
    print(k)
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


# print_board(init_board())


def print_result(winner):
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    endgame = False
    while not endgame:
        get_move(board,player)
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic ; AI esetén get_ai_move
        # print_board(board)
        # # full, has_won - endgame = True, set winner - itt levizsgálni, majd break
        # row, col = get_move(board, 1)
        # mark(board, 1, row, col)
    winner = 0
    print_result(winner)  # printboard itt is kell


def main_menu():
    tictactoe_game('HUMAN-HUMAN')
    pass


if __name__ == '__main__':
    main_menu()
