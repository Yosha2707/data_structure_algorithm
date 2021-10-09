# 2048 Game
# Send Feedback
# 2048 Game
# 2048 is a game and you are expected to implement the move function for this game.
# Arguments passed to the four functions is the matrix which we are using for 2048
# The move function will be returning new matrix after moving the corresponding move.
# Implement All The Four Moves Using These Functions -
# 1. move_up
# 2. move_down
# 3. move_left
# 4. move_right


import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat


def move_up(grid):
    #Implement This Function
    pass

def move_down(grid):
    #Implement This Function
    pass

def move_right(grid):
    #Implement This Function
    pass

def move_left(grid):
    #Implement This Function
    pass


mat = start_game()
mat[1][3] = 2
mat[2][2] = 2
mat[3][0] = 4
mat[3][1] = 8
mat[2][1] = 4
inputs = [int(ele) for ele in input().split()]
for ele in inputs:
    if ele == 1:
        mat = move_up(mat)
    elif ele == 2:
        mat = move_down(mat)
    elif ele == 3:
        mat = move_left(mat)
    else:
        mat = move_right(mat)
    print(mat)