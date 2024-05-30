There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.





class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dp = [[0] * n for _ in range(n)]
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # Max value initially
                if length == 1:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        for k in range(i, j):
                            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        
        return dp[0][n - 1]

# Example usage:
sol = Solution()
print(sol.strangePrinter("aaabbb"))  # Output: 2
print(sol.strangePrinter("aba"))     # Output: 2
