class Solution {
    // compute the number of islands
    int numIslands(char[][] grid) {
        int res = 0;
        int m = grid.length, n = grid[0].length;
        // traversal grid
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    // find an island, the number increases 1
                    res++;
                    // flood the island via dfs
                    dfs(grid, i, j);
                }
            }
        }
        return res;
    }

    // Starting from (i,j), flood all land adjacent to it
    int dfs(char[][] grid, int i, int j) {
        int m = grid.length, n = grid[0].length;
        // out of boundary
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return 1;
        }
        // (i,j) is already water
        if (grid[i][j] == '0') {        
            return 1;
        }
        // flood (i,j) with water (--> mark as visited)
        grid[i][j] = '0';
        // flood land adjacent to (i,j)
        dfs(grid, i + 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i - 1, j);
        dfs(grid, i, j - 1);
        return 1;
    }
}

// leetcode 200
class Topic10GraphProblem1 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        char[][] grid = {
            {'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'}
        };
        System.out.println(sol.numIslands(grid));
    }
}