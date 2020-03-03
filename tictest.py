board = [[1, 2, 0], [0, 0, 0], [0, 0, 0]]

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
        print(row,col)
elif row in "bB":
    row = 1
    if board[row][int(col)-1] != 0:
        print("This place is already taken, choose another coordinate!")
    else:
        print(row,col)
elif row in "cC":
    row = 2
    if board[row][int(col)-1] != 0:
        print("This place is already taken, choose another coordinate!")
    else:
        print(row,col)
