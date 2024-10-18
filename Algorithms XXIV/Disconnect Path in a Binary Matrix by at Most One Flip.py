You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

 

Example 1:


Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 1




class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        self.dirs = [(0, 1), (1, 0)]
        
        # First DFS to check if there is a path
        first = self.dfs(grid, 0, 0)
        
        # Second DFS to check if there is a path again
        second = self.dfs(grid, 0, 0)

        # If there's a path in the second DFS, we cannot cut the path
        return second < 1

    def dfs(self, g, r, c):
        # Check for boundaries and if the cell is blocked
        if r < 0 or r == len(g) or c < 0 or c == len(g[0]) or g[r][c] == 0:
            return 0
        # Check if we reached the bottom-right corner
        if r == len(g) - 1 and c == len(g[0]) - 1:
            return 1
        
        # Mark the cell as visited (change it to 0)
        if not (r == 0 and c == 0):
            g[r][c] = 0

        count = 0
        # Explore the possible directions
        for dr, dc in self.dirs:
            count += self.dfs(g, r + dr, c + dc)
            if count >= 1:
                break  # Early exit if a path is found

        return count        