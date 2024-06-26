Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.





class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]
                
                result[pos1] += total // 10
                result[pos2] = total % 10
        
        # Remove leading zeros
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        
        return ''.join(map(str, result[i:]))
