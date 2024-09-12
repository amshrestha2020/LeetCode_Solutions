You are given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it a palindrome.

Return the length of the maximum length awesome substring of s.

 

Example 1:

Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
Example 2:

Input: s = "12345678"
Output: 1
Example 3:

Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
 

Constraints:

1 <= s.length <= 105
s consists only of digits.




class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        pos = [-1] + [n] * 1024
        res = cur = 0
        for i in range(n):
            cur ^= 1 << int(s[i])
            res = max(res, i - pos[cur])
            for a in range(10):
                res = max(res, i - pos[cur ^ (1 << a)])
            pos[cur] = min(pos[cur], i)
        return res
