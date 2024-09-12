You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.




class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands(grid):
            m, n = len(grid), len(grid[0])
            visited = [[False] * n for _ in range(m)]
            
            def dfs(x, y):
                stack = [(x, y)]
                while stack:
                    i, j = stack.pop()
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] == 1:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
            
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        visited[i][j] = True
                        dfs(i, j)
                        islands += 1
            
            return islands
        
        if count_islands(grid) != 1:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands(grid) != 1:
                        return 1
                    grid[i][j] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    for x in range(m):
                        for y in range(n):
                            if grid[x][y] == 1:
                                grid[x][y] = 0
                                if count_islands(grid) != 1:
                                    return 2
                                grid[x][y] = 1
                    grid[i][j] = 1
        
        return 2
