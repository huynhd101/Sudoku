def solve_backtrack(board):


def check(board, position, guess):
    """
    Returns True if the guess is a valid number to be placed at position
    """

    #Check Row
    for i in range(len(board[position[0]])):
        if board[position[0]][i] == guess and i != position[1]:
            return False
    

    #Check Column
    for i in range(len(board)):
        if board[i][position[1]] == guess and i != position[0]:
            return False

    #Check 3x3 Square
    #integer divide to find which square we are in
    square_row = position[0] // 3
    square_col = position[1] // 3

    for i in range(square_row*3, square_row + 3):
        for j in range(square_col * 3, square_col*3 + 3):
            if board[i][j] == guess and (i,j) != position:
                return False

    return True

