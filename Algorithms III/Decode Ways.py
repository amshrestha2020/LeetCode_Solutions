A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).




class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to decode an empty string
        dp[1] = 1  # Base case: single character string (not '0')
        
        for i in range(2, n + 1):
            # Single digit decode is possible
            if 1 <= int(s[i - 1:i]) <= 9:
                dp[i] += dp[i - 1]
            # Two digit decode is possible
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]

# Example usage
solution = Solution()
print(solution.numDecodings("12"))   # Output: 2
print(solution.numDecodings("226"))  # Output: 3
print(solution.numDecodings("06"))   # Output: 0
