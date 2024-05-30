You are given a string s of length n where s[i] is either:

'D' means decreasing, or
'I' means increasing.
A permutation perm of n + 1 integers of all the integers in the range [0, n] is called a valid permutation if for all valid i:

If s[i] == 'D', then perm[i] > perm[i + 1], and
If s[i] == 'I', then perm[i] < perm[i + 1].
Return the number of valid permutations perm. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: s = "DID"
Output: 5
Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
Example 2:

Input: s = "D"
Output: 1
 

Constraints:

n == s.length
1 <= n <= 200
s[i] is either 'I' or 'D'.






class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Base case: single length permutation
        for j in range(n + 1):
            dp[0][j] = 1
        
        for i in range(1, n + 1):
            if s[i - 1] == 'I':
                running_sum = 0
                for j in range(n - i + 1):
                    running_sum = (running_sum + dp[i - 1][j]) % MOD
                    dp[i][j] = running_sum
            else:  # s[i - 1] == 'D'
                running_sum = 0
                for j in range(n - i, -1, -1):
                    running_sum = (running_sum + dp[i - 1][j + 1]) % MOD
                    dp[i][j] = running_sum
        
        return dp[n][0]

# Example usage:
solution = Solution()
print(solution.numPermsDISequence("DID"))  # Output: 5
print(solution.numPermsDISequence("D"))    # Output: 1
