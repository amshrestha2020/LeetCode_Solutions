An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199
 

Constraints:

1 <= num.length <= 35
num consists only of digits.
 

Follow up: How would you handle overflow for very large input integers?
    




class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def backtrack(start, first, second):
            if start == n:
                return True
            for i in range(start, n):
                if i > start and num[start] == '0':  # leading zero
                    break
                curr = int(num[start:i+1])
                if curr > first + second:
                    break
                if curr == first + second and backtrack(i+1, second, curr):
                    return True
            return False

        for i in range(1, n):
            if i > 1 and num[0] == '0':  # leading zero
                break
            first = int(num[:i])
            for j in range(i+1, n):
                if j > i+1 and num[i] == '0':  # leading zero
                    break
                second = int(num[i:j])
                if backtrack(j, first, second):
                    return True
        return False
