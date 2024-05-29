You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:

Input: s = "leetcode", k = 8
Output: 0
 

Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters.



from typing import List

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        mod = 10**9 + 7
        cost = [[0]*n for _ in range(n)]
        dp = [[float('inf')]*n for _ in range(k)]
        
        # Pre-calculate the cost to change s[i:j] into a palindrome
        for span in range(2, n+1):
            for i in range(n-span+1):
                j = i + span - 1
                cost[i][j] = cost[i+1][j-1] + (s[i] != s[j])
        
        # Dynamic programming
        for i in range(n):
            dp[0][i] = cost[0][i]
            if i < k:
                dp[i][i] = 0
            for j in range(1, min(i+1, k)):
                for m in range(i):
                    dp[j][i] = min(dp[j][i], dp[j-1][m] + cost[m+1][i])
        
        return dp[k-1][n-1]
