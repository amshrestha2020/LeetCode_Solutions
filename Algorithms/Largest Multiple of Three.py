Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
 

Constraints:

1 <= digits.length <= 104
0 <= digits[i] <= 9





class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        sum_digits = sum(digits)
        
        remainder1 = []
        remainder2 = []
        
        for digit in digits:
            if digit % 3 == 1:
                remainder1.append(digit)
            elif digit % 3 == 2:
                remainder2.append(digit)
        
        if sum_digits % 3 == 1:
            if remainder1:
                digits.remove(remainder1[-1])
            else:
                if len(remainder2) >= 2:
                    digits.remove(remainder2[-1])
                    digits.remove(remainder2[-2])
                else:
                    return ""
        elif sum_digits % 3 == 2:
            if remainder2:
                digits.remove(remainder2[-1])
            else:
                if len(remainder1) >= 2:
                    digits.remove(remainder1[-1])
                    digits.remove(remainder1[-2])
                else:
                    return ""
        
        digits.sort(reverse=True)
        
        if digits and digits[0] == 0:
            return "0"
        
        return "".join(map(str, digits))


