Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.



class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        pos = [-1] * (1 << 5)  # 1 << 5 = 32, which is enough to represent 5 vowels' odd/even information
        pos[0] = 0
        ans, status = 0, 0
        for i, ch in enumerate(s, 1):
            if ch in 'aeiou':
                status ^= 1 << 'aeiou'.find(ch)  # flip the bit
            if pos[status] >= 0:
                ans = max(ans, i - pos[status])
            else:
                pos[status] = i
        return ans
