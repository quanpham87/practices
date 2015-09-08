def validSolutionV3(board):
    # new solution that utilize python list's comprehensive
    check = range(1, 10)
    # validate blocks
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if sorted(block) != check:
                return False
    # validate rows and columns
    for i in range(0, 9):        
        if sorted(board[i][0:9]) != check or sorted([row[i] for row in board]) != check:
            return False
    return True
    
def validSolutionV2(board):
    # most minified
    check = range(1, 10)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if sorted(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]) != check or \
                sorted(board[i][0:9]) != check or sorted([row[i] for row in board]) != check or \
                sorted(board[i+1][0:9]) != check or sorted([row[i+1] for row in board]) != check or \
                sorted(board[i+2][0:9]) != check or sorted([row[i+2] for row in board]) != check:
                return False
    return True
    
def validSolution(board):
    validCheck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # pick out the 3x3 matrix to test on
    # go through each item and mark validCheck[item - 1] = 1 if == 0 else return false
    # 1st check the 3x3 blocks
    i = 0
    j = 0
    while i < 9:
        while j < 9:
            matrix = [
                board[i][j],
                board[i][j+1],
                board[i][j+2],
                board[i+1][j],
                board[i+1][j+1],
                board[i+1][j+2],
                board[i+2][j],
                board[i+2][j+1],
                board[i+2][j+2]
            ]
            for m in matrix:
                if m == 0:
                    return False
                if validCheck[m-1] == 0:
                    validCheck[m-1] = 1
                else:
                    return False
            for m in validCheck:
                if m != 1:
                    return False
            validCheck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            j+=3
        j=0
        i+=3
    # check the rows and columns
    for i in range(9):
        rowCheck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        colCheck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            if rowCheck[board[i][j]-1] == 0:
                rowCheck[board[i][j]-1] = 1
            else:
                return False
            if colCheck[board[j][i]-1] == 0:
                colCheck[board[j][i]-1] = 1
            else:
                return False
        for m in range(9):
            if rowCheck[m] != 1 or colCheck[m] != 1:
                return False
    return True
