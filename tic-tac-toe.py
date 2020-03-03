# import os
# import time
# import pygame
# import random


def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # row the outer, column the inner list(s)
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if (0 <= row < 2) and (0 <= col < 2):
        if board[row][col] == 0:
            board[row][col] = player
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    k = 0
    for i in board:
        k += i.count(0)
    print(k)
    if k == 0:
        return True
    else:
        return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
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


print_board(init_board())


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    endgame = False
    while not endgame:
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic ; AI esetén get_ai_move
        print_board(board)
        # full, has_won - endgame = True, set winner - itt levizsgálni, majd break
        row, col = get_move(board, 1)
        mark(board, 1, row, col)
    winner = 0
    print_result(winner)  # printboard itt is kell


def main_menu():
    # tictactoe_game('HUMAN-HUMAN')
    pass


if __name__ == '__main__':
    main_menu()
