# 2352. Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        sum = 0
        # column_grid = [[0]*n]*n # initializing the array like above results in issues
        
        # below reinitializing the column grid:
        column_grid = [[0]*n for _ in range(n)]
        for r in range(0,n):
            for c in range(0,n):
                column_grid[r][c] = grid[c][r]
        hash_map = defaultdict(int)
        for row in grid:
            row_str = ''.join(str(row))
            hash_map[row_str] += 1
        for column in column_grid:
            col_str = ''.join(str(column))
            if(col_str in hash_map):
                # sum is how many ever times it is present as a row + sum
                sum += hash_map.get(col_str)
        return sum
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    print('\nTest Case #1')
    print(f'solution.equalPairs(grid={grid}) = {solution.equalPairs(grid=grid)}')
    print('Expected Output: 1')

    # Test Case #2
    # Inputs:
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print('\nTest Case #2')
    print(f'solution.equalPairs(grid={grid}) = {solution.equalPairs(grid=grid)}')
    print('Expected Output: 3')

    # Test Case #3
    # Inputs:
    grid = [[13,13],[13,13]]
    print('\nTest Case #3')
    print(f'solution.equalPairs(grid={grid}) = {solution.equalPairs(grid=grid)}')
    print('Expected Output: 4')

    # Test Case #4
    # Inputs:
    grid = [[3,3,3,6,18,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[1,1,1,11,19,1,1,1,1,1],[3,3,3,18,19,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,1,6,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3]]
    print('\nTest Case #4')
    print(f'solution.equalPairs(grid={grid}) = {solution.equalPairs(grid=grid)}')
    print('Expected Output: 48')

    print("\nLeetCode Runtime: 82ms")
    print("LeetCode Beats: 35.51%")