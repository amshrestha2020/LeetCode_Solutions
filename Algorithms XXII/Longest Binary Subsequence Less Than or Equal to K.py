You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= k <= 109



class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Reverse the string
        s = s[::-1]
        
        n = len(s)
        
        # Initialize the dp array with tuples (length, value)
        dp = [(0, 0)] * n
        
        # Fill the dp array based on the binary string
        for i in range(n):
            if s[i] == '0':
                dp[i] = (1, 0)
            else:
                dp[i] = (1, 1)

        res = 0
        
        # Dynamic programming to find the longest subsequence
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                curr_len, curr_val = dp[j]
                
                if s[i] == '1' and (curr_val + (1 << curr_len)) <= k:
                    if (curr_len + 1) > dp[i][0]:
                        dp[i] = (curr_len + 1, curr_val + (1 << curr_len))
                elif s[i] == '0' and curr_val <= k:
                    if (curr_len + 1) > dp[i][0]:
                        dp[i] = (curr_len + 1, curr_val)

            res = max(res, dp[i][0])

        if n == 1:
            return 1
        
        return res        