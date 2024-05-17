Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

 

Example 1:

Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:

Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
Output: 104860361
Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 109 + 7.
 

Constraints:

1 <= s.length <= 1000
s[i] is either 'a', 'b', 'c', or 'd'.





class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # Create a dp table
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single letter palindromes
        for i in range(n):
            dp[i][i] = 1
        
        # Process all substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    left = i + 1
                    right = j - 1
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[j]:
                        right -= 1
                    if left > right:  # no same char in s[i+1:j]
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 2
                    elif left == right:  # one same char in s[i+1:j]
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 1
                    else:  # more than one same char in s[i+1:j]
                        dp[i][j] = 2 * dp[i + 1][j - 1] - dp[left + 1][right - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                
                dp[i][j] = (dp[i][j] + MOD) % MOD
        
        return dp[0][n - 1]

# Example usage
solution = Solution()
print(solution.countPalindromicSubsequences("bccb"))  # Output: 6
print(solution.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"))  # Output: 104860361
