You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

 

Example 1:

Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
Example 2:

Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
 

Constraints:

-1015 <= num <= 1015




class Solution:
    def smallestNumber(self, num: int) -> int:
        # Check if the number is negative
        if num < 0:
            # For negative numbers, sort digits in descending order
            digits = sorted(str(-num), reverse=True)
            result = -int(''.join(digits))
        else:
            # For positive numbers, sort digits in ascending order
            digits = sorted(str(num))
            # If the first digit is '0', find the first non-zero digit
            if digits[0] == '0':
                # Find the first non-zero digit and swap with the first digit
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        # Swap first zero with the first non-zero digit
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            result = int(''.join(digits))
        
        return result        