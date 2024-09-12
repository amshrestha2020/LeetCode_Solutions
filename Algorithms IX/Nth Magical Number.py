A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
 

Constraints:

1 <= n <= 109
2 <= a, b <= 4 * 104





import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        LCM = a * b // math.gcd(a, b)

        def count(x):
            # Returns how many magical numbers are <= x.
            return x // a + x // b - x // LCM

        # Binary search for the smallest x such that count(x) >= n.
        lo = 0
        hi = 10**15
        while lo < hi:
            mi = (lo + hi) // 2
            if count(mi) < n:
                lo = mi + 1
            else:
                hi = mi

        return lo % MOD
