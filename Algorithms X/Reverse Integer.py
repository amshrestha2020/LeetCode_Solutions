Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1





class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        result = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
                return 0
            if result < MIN_INT // 10 or (result == MIN_INT // 10 and digit < -8):
                return 0
            
            result = result * 10 + digit
            
        return result * sign

# Test cases
solution = Solution()
print(solution.reverse(123))  # Output: 321
print(solution.reverse(-123)) # Output: -321
print(solution.reverse(120))  # Output: 21
