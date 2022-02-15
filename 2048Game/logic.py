import  random
# creat the function for start the game
def startgame():
    mat  = []
    for i in range(4):
        mat.append([0]*4) # creat a 4 * 4 empty matrix
    return mat
# creat a function for the genrating  2 in ramdom index and chek the space is empty or not
def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while (mat[r][c] != 0 ):
         r = random.randint(0,3)
         c = random.randint(0,3)
    mat[r][c] = 2

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
def merg(mat):    # here we can add the 2 number in every moment if 2 number is eual and not wual to zero
    change = False

    for i in range(4):
        for j in range(3):
            if (mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
                mat[i][j] = mat[i][j]*2  # multiwith 2 because we can only add the same number
                mat[i][j+1] = 0
                change = True # if the above condition is going to true then chnage is true
    return mat,change


def compress(mat):
    change = False
    new_mat = [] # creat a 4 * 4 new empty matrix
    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    chnage = True
                pos += 1
    return new_mat,chnage
def move_up(grid):
    tranpose_grid = transpose(grid)
    new_grid,change1 = compress(tranpose_grid)
    new_grid,change2 = merg(new_grid)
    change = change1 , change2
    new_grid = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,change
def move_down(grid):
    tranpose_grid = transpose(grid)
    reversed_grid = reverse(tranpose_grid)
    new_grid,change1 = compress(reversed_grid)
    new_grid,change2 = merg(new_grid)
    change = change1 or change2
    new_grid = compress(new_grid)
    final_reverse_grid = reverse(new_grid)
    final_grid = transpose(final_reverse_grid)
    return final_grid

def move_right(grid):
    reverse_grid = reverse(grid)
    new_grid,change1 = compress(reverse_grid)
    new_grid,change2 = compress(new_grid)
    change = change1 or change2
    new_grid = merg(new_grid)
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,change



def move_left(grid): # we can move left
    new_grid,change1 = compress(grid)
    new_grid,change2 = merg(new_grid)
    change = change1 or change2
    new_grid,temp = compress(new_grid)
    return  new_grid,change
# check the current state of the game
def get_current_state(mat):
    # chek if 2048 is present in the matrix or not  if it is then won the game
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return "hey you WON the Game"
    # chek for empty space in the matrix
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0 ):
                return "game  not over"
    # chek for every row and col is there any ele is same in the 4 driction expet last row and col
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "game  not over "
    # check for last row
    for j in range(3):
        if (mat[3][j] == mat[3][j+1]):
            return "game  not over "
    # check of rthe col
    for i in range(3):
        if (mat[i][3] == mat[i+1][3]):
            return "game not over "
    # game over
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "Game Over"

    return "lost"




 # start the game
mat = startgame()
print(mat)
# # adding to at the redom position
# add_new_2(mat)
# print(mat)
# add_new_2(mat)
# print(mat)
#
# mat = move_up(mat)
# print(mat)
# mat = move_left(mat)
# print(mat)
# mat = move_down(mat)
# print(mat)
# mat = move_right(mat)
# print(mat)