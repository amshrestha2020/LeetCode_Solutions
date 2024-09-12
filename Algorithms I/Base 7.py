Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107




class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        
        result = []
        while num > 0:
            remainder = num % 7
            result.append(str(remainder))
            num //= 7
        
        if negative:
            result.append('-')
        
        return ''.join(result[::-1])

# Example usage
solution = Solution()
print(solution.convertToBase7(100))  # Output: "202"
print(solution.convertToBase7(-7))   # Output: "-10"

