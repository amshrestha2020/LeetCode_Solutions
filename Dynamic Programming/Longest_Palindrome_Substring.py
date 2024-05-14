Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.



class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        longest_len = 1
        start = 0
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # check for sub-string of length 2. 
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                longest_len = 2
        # check for lengths greater than 2. 
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    longest_len = length
        return s[start:start + longest_len]

