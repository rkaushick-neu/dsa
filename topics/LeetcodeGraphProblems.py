# Problem 0 - Leetcode
# Given a binary tree, find its minimum depth. The minimum depth is
# the number of nodes along the shortest path from the root node
# down to the nearest leaf node. Note: A leaf is a node with no
# children.

# Problem 1 - Leetcode 200

# Given an m x n 2D binary self.grid which represents a map of ’1’s (land)
# and ’0’s (water), return the number of islands. An island is
# surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the self.grid
# are all surrounded by water.

class Leetcode200:
    def __init__(self, grid: list[list[str]]) -> None:
        self.grid = grid

    # using Flood Fill on top of DFS
    def flood_fill_dfs(self, i:int, j:int):
        m = len(self.grid)
        n = len(self.grid[0])
        if(i<0 or j<0 or i>=m or j>=n):
            return
        if(self.grid[i][j] == "0"):
            return
        self.grid[i][j] = "0"
        self.flood_fill_dfs(i-1, j) # up
        self.flood_fill_dfs(i+1, j) # down
        self.flood_fill_dfs(i, j-1) # left
        self.flood_fill_dfs(i, j+1) # right
        return

    def find_islands(self) -> int:
        sum_of_islands = 0
        m = len(self.grid)
        n = len(self.grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if(self.grid[i][j] == "1"):
                    self.flood_fill_dfs(i, j)
                    sum_of_islands += 1
        return sum_of_islands

# Problem 2 -  Leetcode 1254

# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally 
# connected group of 0s and a closed island is an island totally (all left, top, right, bottom) 
# surrounded by 1s.

# Return the number of closed islands.

class Leetcode1254:
    def __init__(self) -> None:
        pass


# Problem 3 - L

# Problem 4 - Leetcode 695

# Problem 5 - Leetcode 1905

# Adjacency List for real world problems

if __name__ == '__main__':
    # Test case 1
    grid1 = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ]

    # Test case 2
    grid2 = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
            ]
    
    tc_1_lc_200 = Leetcode200(grid1)
    print(tc_1_lc_200.find_islands())
    tc_2_lc_200 = Leetcode200(grid=grid2)
    print(tc_2_lc_200.find_islands())
