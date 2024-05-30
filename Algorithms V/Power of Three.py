Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-2^31 <= n <= 2^31 - 1




import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        # Calculate log base 3 of n and compare it to its integer representation
        log_n = math.log(n, 3)
        return abs(log_n - round(log_n)) < 1e-10
