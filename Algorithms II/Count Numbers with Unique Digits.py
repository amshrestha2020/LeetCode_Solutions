Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1
 

Constraints:

0 <= n <= 8




class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: 
            return 1

        # For n = 1, there are 10 unique-digit numbers: 0, 1, 2, ..., 9
        result = 10
        unique_digits = 9
        available_number = 9

        while n > 1 and available_number > 0:
            unique_digits = unique_digits * available_number
            result += unique_digits
            available_number -= 1
            n -= 1

        return result

