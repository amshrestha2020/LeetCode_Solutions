The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
 

Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104




class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Convert k to a list of its digits
        k_digits = [int(digit) for digit in str(k)]
        
        # Initialize the result list to store the sum
        result = []
        
        # Initialize indices for num and k_digits
        i = len(num) - 1
        j = len(k_digits) - 1
        
        carry = 0
        
        # Perform addition digit by digit
        while i >= 0 or j >= 0 or carry > 0:
            # Get the digit from num or 0 if index out of range
            num_digit = num[i] if i >= 0 else 0
            
            # Get the digit from k_digits or 0 if index out of range
            k_digit = k_digits[j] if j >= 0 else 0
            
            # Calculate the sum of current digits and carry
            digit_sum = num_digit + k_digit + carry
            
            # Update carry and append the least significant digit to the result
            carry = digit_sum // 10
            result.append(digit_sum % 10)
            
            # Move to the next digit in num and k_digits
            i -= 1
            j -= 1
        
        # Reverse the result list to get the correct order
        return result[::-1]
