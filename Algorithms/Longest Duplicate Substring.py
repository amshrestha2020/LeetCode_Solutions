Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

 

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
 

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.




from typing import List

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Binary search the length of longest duplicate substring
        left, right = 1, len(s)
        while left <= right:
            mid = (left + right) // 2
            if self.check(s, mid) is not None:
                left = mid + 1
            else:
                right = mid - 1

        start = self.check(s, right)
        return s[start: start + right]

    def check(self, s: str, length: int) -> int:
        # Check whether there exists a duplicate substring of certain length
        MOD = 2**63 - 1
        base = 26
        hash = 0
        seen = set()

        # Compute the hash of first 'length' characters
        for i in range(length):
            hash = (hash * base + ord(s[i])) % MOD
        seen.add(hash)

        # Compute the hash of next substrings with rolling hash method
        power = pow(base, length, MOD)
        for i in range(length, len(s)):
            hash = ((hash * base - ord(s[i - length]) * power) + ord(s[i])) % MOD
            if hash in seen:
                return i - length + 1
            seen.add(hash)

        return None
