import colors as c

def winner(mat):
    win = None
    for count in range(len(mat[0])):
        if mat[count][0] == mat[count][1] == mat[count][2]:
            win = True
        if mat[0][count] == mat[1][count] == mat[2][count]:
            win = True
    if mat[0][0] == mat[1][1] == mat[2][2]:
        win = True
    if mat[0][2] == mat[1][1] == mat[2][0]:
        win = True
    return win

find = None
mat = None
lastMove = None
options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
playernum = 1

board = """
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9 
"""

print(board)

while options != []:
    while lastMove not in options:
        lastMove = input('Player ' + str(playernum) + ': Pick a spot on the board that isn\'t taken (1 - 9): ')     
    if playernum == 1:
        board = board.replace(str(lastMove), 'X')
        playernum += 1
    elif playernum == 2:
        board = board.replace(str(lastMove), 'O')
        playernum -= 1

    find = board[2:14:4] + board[25:35:4] + board[48:58:4]
    mat = [[str(find[0]), str(find[1]), str(find[2])], [str(find[3]), str(find[4]), str(find[5])], [str(find[6]), str(find[7]), str(find[8])]]
    options.remove(lastMove)
    print(board)
    
    if winner(mat) == True:
        if playernum == 1:
            print('Player 2 has won the game.')
        else:
            print('Player 1 has won the game.')
        break

if winner(mat) != True:
    print('You tied')