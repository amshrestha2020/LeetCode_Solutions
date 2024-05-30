You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.




class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = -1
            bfs.append((i, j))
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        def firstIsland():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j

        n = len(grid)
        bfs = []
        dfs(*firstIsland())

        dist = 0
        while bfs:
            new = []
            for x, y in bfs:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = -1
                            new.append((nx, ny))
                        elif grid[nx][ny] == 1:
                            return dist
            dist += 1
            bfs = new
