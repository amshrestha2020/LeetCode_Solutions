Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.

 

Example 1:

Input: num = 443
Output: true
Explanation: 172 + 271 = 443 so we return true.
Example 2:

Input: num = 63
Output: false
Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.
Example 3:

Input: num = 181
Output: true
Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.
 

Constraints:

0 <= num <= 105




class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for x in range(num + 1):
            # Reverse the digits of x
            reversed_x = int(str(x)[::-1])
            # Check if x + reversed_x equals num
            if x + reversed_x == num:
                return True
        return False        