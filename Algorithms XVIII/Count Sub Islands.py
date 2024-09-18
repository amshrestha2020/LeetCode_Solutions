You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.




class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            # If out of bounds or it's water in grid2, stop the DFS.
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            
            # Mark the cell as visited in grid2.
            grid2[i][j] = 0
            
            # Assume it's a sub-island unless we find a cell in grid1 that is water.
            is_sub_island = True
            if grid1[i][j] == 0:
                is_sub_island = False
            
            # Explore in 4 directions (up, down, left, right).
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i, j + 1)
            is_sub_island &= dfs(i, j - 1)
            
            return is_sub_island
        
        m, n = len(grid1), len(grid2[0])
        sub_islands_count = 0
        
        # Loop through every cell in grid2
        for i in range(m):
            for j in range(n):
                # If the current cell is land in grid2, start a DFS.
                if grid2[i][j] == 1:
                    # If the DFS confirms that it's a sub-island, increment the counter.
                    if dfs(i, j):
                        sub_islands_count += 1
        
        return sub_islands_count        