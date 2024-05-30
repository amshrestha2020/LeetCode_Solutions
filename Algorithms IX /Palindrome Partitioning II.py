Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.



class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:  # If the whole string is a palindrome, no cuts are needed
            return 0

        n = len(s)
        dp = [0]*n
        isPalindrome = [[False]*n for _ in range(n)]

        for i in range(n):
            min_val = i
            for j in range(i+1):
                if s[i] == s[j] and (i-j < 2 or isPalindrome[j+1][i-1]):
                    isPalindrome[j][i] = True
                    min_val = 0 if j == 0 else min(min_val, dp[j-1] + 1)
            dp[i] = min_val

        return dp[-1]
