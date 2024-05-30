You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
1 <= n <= 5000




class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0, 0] for _ in range(n+1)]
        dp[1][0] = 6
        dp[1][1] = 6
        for i in range(2, n+1):
            dp[i][0] = (3*dp[i-1][0] + 2*dp[i-1][1]) % MOD
            dp[i][1] = (2*dp[i-1][0] + 2*dp[i-1][1]) % MOD
        return (dp[n][0] + dp[n][1]) % MOD
