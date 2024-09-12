Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.





class Solution:
    def ways(self, pizza, k):
        m, n = len(pizza), len(pizza[0])
        dp = [[[-1]*n for _ in range(m)] for _ in range(k)]
        preSum = [[0]*(n+1) for _ in range(m+1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                preSum[r][c] = preSum[r][c+1] + preSum[r+1][c] - preSum[r+1][c+1] + (pizza[r][c] == 'A')

        return self.dfs(m, n, k-1, 0, 0, dp, preSum)

    def dfs(self, m, n, k, r, c, dp, preSum):
        if preSum[r][c] == 0: return 0
        if k == 0: return 1
        if dp[k][r][c] != -1: return dp[k][r][c]
        ans = 0

        for nr in range(r + 1, m):
            if preSum[r][c] - preSum[nr][c] > 0:
                ans = (ans + self.dfs(m, n, k - 1, nr, c, dp, preSum)) % 1000000007
        for nc in range(c + 1, n):
            if preSum[r][c] - preSum[r][nc] > 0:
                ans = (ans + self.dfs(m, n, k - 1, r, nc, dp, preSum)) % 1000000007

        dp[k][r][c] = ans
        return ans
