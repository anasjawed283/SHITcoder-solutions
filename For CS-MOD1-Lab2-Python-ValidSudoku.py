# import sys
# def doSomething(inval):
#     #Do Something
#     return outval
# inputVal = input()    
# outputVal = doSomething(input)
# print (output)
                                                                                                                            

def is_valid_sudoku(board):
    def is_valid_line(line):
        # Check if a line (row or column) contains the numbers 1-9 exactly once
        seen = set()
        for num in line:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    # Check each row
    for row in board:
        if not is_valid_line(row):
            return "NO"

    # Check each column
    for col in range(9):
        if not is_valid_line([board[row][col] for row in range(9)]):
            return "NO"

    # Check each 3x3 sub-box
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_line(sub_box):
                return "NO"

    return "YES"

# Input reading
n = int(input())
sudoku_board = [input().split() for _ in range(n)]

# Output
print(is_valid_sudoku(sudoku_board))
