Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].




class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = [str(10**l + d) for l in [length - 1, length] for d in [-1, 1]]
        prefix = int(n[:(length + 1) // 2])
        for start in map(str, [prefix - 1, prefix, prefix + 1]):
            candidates.append(start + [start, start[:-1]][length & 1][::-1])
        candidates.sort(key=lambda x: (abs(int(x) - int(n)), int(x)))
        return next(x for x in candidates if x != n)
