def solve_backtrack(board):


def check(board, position, guess):
    """
    Returns True if the guess is a valid number to be placed at position
    Parameters:
    -board (2D list): a board of numbers where empty spaces are represented by '0'
    -position ((int, int)): row and column of where we are checking for validity
    -guess (int): the value we are guessing
    Returns:
    -boolean
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

def find_empty(board):
    """
    Finds on the board an empty spot
    Parameters:
    board (2D list): a board of numbers where empty spaces are represented by '0'
    Returns:
    (int, int) row and col
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None
