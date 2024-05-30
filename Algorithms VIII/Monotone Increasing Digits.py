An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 

Example 1:

Input: n = 10
Output: 9
Example 2:

Input: n = 1234
Output: 1234
Example 3:

Input: n = 332
Output: 299
 

Constraints:

0 <= n <= 109




class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))
        i = 1
        while i < len(digits) and digits[i-1] <= digits[i]:
            i += 1
        while 0 < i < len(digits) and digits[i-1] > digits[i]:
            digits[i-1] -= 1
            i -= 1
        for j in range(i+1, len(digits)):
            digits[j] = 9
        return int(''.join(map(str, digits)))
