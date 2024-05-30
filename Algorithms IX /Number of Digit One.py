Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 109




class Solution:
    def countDigitOne(self, n: int) -> int:
        left, right, m = n, 0, 1
        ones = 0
        while left > 0:
            left, curr = divmod(left, 10)
            ones += left * m
            if curr == 1:
                ones += right + 1
            elif curr > 1:
                ones += m
            right += curr * m
            m *= 10
        return ones
