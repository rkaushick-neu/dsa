# 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # we just need to check one box per row, column and grid

        # this way
        # [0,0], [1,3], [2,6]
        # [3,1], [4,4], [5,7]
        # [6,2], [7,5], [8,8]

        # which can be written as:
        # [0, 0*3%8], [1, 1*3%8], [2, 2*3%8]
        # [3, 3*3%8], [4, 4*3%8], [5, 5*3%8]
        # [6, 6*3%8], [7, 7*3%8], { [8, 8*3%8] --> this doesn't work }

        # if it is 8th, we will just force it to check [8,8]

        for i in range(0, 9):
            if(i == 8):
                # check for [8,8]
                if(not Solution.check_row(i, i, board) or not Solution.check_col(i, i, board) or not Solution.check_grid(i, i, board)):
                    return False
            else:
                if(not Solution.check_row(i, (i*3%8), board) or not Solution.check_col(i, (i*3%8), board) or not Solution.check_grid(i, (i*3%8), board)):
                    return False
        return True

    def check_row(row: int, col: int, board: list[list[str]]) -> bool:
        other_nums = set()
        for i in range(0, 9):
            num = board[row][i]
            if(num != '.'):
                if(num in other_nums):
                    return False
                else:
                    other_nums.add(num)
        return True

    def check_col(row: int, col: int, board: list[list[str]]) -> bool:
        other_nums = set()
        for i in range(0, 9):
            num = board[i][col]
            if(num != '.'):
                if(num in other_nums):
                    return False
                else:
                    other_nums.add(num)
        return True
            
    def get_min_and_max(row_or_col: int) -> list[int]:
        if(row_or_col>=0 and row_or_col<3):
            min_element = 0
            max_element = 3
        elif(row_or_col>=3 and row_or_col<6):
            min_element = 3
            max_element = 6
        else:
            min_element = 6
            max_element = 9
        return [min_element, max_element]
    
    def check_grid(row: int, col: int, board: list[list[str]]) -> bool:
        # find the grid to search
        min_row, max_row = Solution.get_min_and_max(row)
        min_col, max_col = Solution.get_min_and_max(col)        
        grid_nums = set()
        for i in range(min_row, max_row):
            for j in range(min_col, max_col):
                num = board[i][j]
                if(num != '.'):
                    if(num in grid_nums):
                        return False
                    else:
                        grid_nums.add(num)
        return True
    
if __name__ == '__main__':
    solution = Solution()

    print("Approach 1: Complement")
    # Test Case #1
    # Inputs:
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print('\nTest Case #1')
    print(f'solution.isValidSudoku(board="{board}") = {solution.isValidSudoku(board=board)}')
    print('Expected Output: True')

    # Test Case #2
    # Inputs:
    board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print('\nTest Case #2')
    print(f'solution.isValidSudoku(board="{board}") = {solution.isValidSudoku(board=board)}')
    print('Expected Output: False')