Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

Constraints:

1 <= n <= 231 - 1





class Solution:
    def findNthDigit(self, n: int) -> int:
        # Step 1: Find the number of digits in the number where the nth digit is
        digit_level = 1
        while n > digit_level * 9 * 10**(digit_level - 1):
            n -= digit_level * 9 * 10**(digit_level - 1)
            digit_level += 1

        # Step 2: Find the exact number where the nth digit is
        num = 10**(digit_level - 1) + (n - 1) // digit_level

        # Step 3: Find the exact digit and return
        return int(str(num)[(n - 1) % digit_level])
