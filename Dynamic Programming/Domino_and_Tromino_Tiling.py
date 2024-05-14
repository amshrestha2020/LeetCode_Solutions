You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 1000



class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp2 = [0] * (n + 1)
        dp3 = [0] * (n + 1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * dp2[i-1]) % MOD
            dp2[i] = (dp[i-2] + dp3[i-1]) % MOD
            dp3[i] = (dp[i-2] + dp2[i-1]) % MOD
        
        return dp[n]

# Example usage
solution = Solution()
print(solution.numTilings(3))  # Output: 5
print(solution.numTilings(1))  # Output: 1


