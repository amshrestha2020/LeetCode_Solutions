Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = 1

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                # palindrome condition
                if s[start] == s[end]:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

        return dp[0][n - 1]  # longest palindromic subsequence

