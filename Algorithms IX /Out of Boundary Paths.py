There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n




class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]
        
        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if x < 0 or x >= m or y < 0 or y >= n:
                            dp[move][i][j] += 1
                        else:
                            dp[move][i][j] = (dp[move][i][j] + dp[move - 1][x][y]) % MOD
                            
        return dp[maxMove][startRow][startColumn]

