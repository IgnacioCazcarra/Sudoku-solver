board = [
[0,3,7,2,0,0,6,5,0],
[2,0,0,0,5,0,0,0,3],
[0,0,5,6,7,0,0,8,0],
[0,0,3,0,0,0,0,0,0],
[0,2,0,0,3,0,0,7,0],
[4,7,0,5,0,8,0,0,2],
[0,0,6,0,0,0,3,9,7],
[0,0,8,0,0,0,0,2,5],
[3,0,2,0,0,0,0,4,0]
]


def draw_board(board):

    for i in range(len(board)):
        if i%3==0 and i!=0:
            print('--------------------------------')
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print(' | ',end="")
            if j==8:
                print(" " + str(board[i][j]))
            else: print(" " + str(board[i][j]) + " ",end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
    return None

def valid_number(board, number, pos):
    #Check row
    for j in range(len(board[0])):
        #pos[0] es i que retornamos en find_empty (solo i, j no)
        #pos[1] != j porque sino estariamos buscando en el mismo lugar donde queremos reemplazar el numero
        if board[pos[0]][j] == number and pos[1] != j:
            return False 
    
    #Check column
    for i in range(len(board)):
        if board[i][pos[1]] == number and pos[0] != i:
            return False

    #Check 3x3 square
    #Vamos a pensar los cuadrados como una matriz 3x3 donde esta el cuadrado [0][0],[0][1],[0][2] y asi
    #Con el // lo que hacemos es dividir sin decimales, or lo que la columna 0,1,2 nos va a dar 0, 3,4,5 darian 1 y 6,7,8 darian 2
    #por lo que sabemos (por ejemplo) que estamos en alguno de los 3 cuadrados de arriba
    pos_x = pos[1] // 3
    pos_y = pos[0] // 3

    for i in range(pos_y*3, pos_y*3 + 3):
        for j in range(pos_x*3, pos_x*3 + 3):
            if board[i][j] == number and (i,j) != pos:
                return False

    return True

def solve(board):

    if not find_empty(board):
        return True
    else:
        (i,j) = find_empty(board)

    for possible_number in range(1,10):
        if(valid_number(board,possible_number,(i,j))):
            
            board[i][j] = possible_number   
            
            if solve(board):
                return True
            else:
                board[i][j] = 0
    return False

def sudoku():
    draw_board(board)
    print("*"*33)
    solve(board)
    draw_board(board)


if __name__ == "__main__":
    sudoku()