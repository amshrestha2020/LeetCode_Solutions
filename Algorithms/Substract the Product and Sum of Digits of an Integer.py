Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5





class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Convert the integer to string for easy access to each digit
        str_n = str(n)
        
        # Initialize product and sum
        product = 1
        sum_ = 0
        
        # Iterate over each digit in the string
        for digit in str_n:
            # Convert the digit back to an integer
            int_digit = int(digit)
            
            # Update product and sum
            product *= int_digit
            sum_ += int_digit
        
        # Return the difference between product and sum
        return product - sum_
