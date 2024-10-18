You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.



class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = []  # This will store the final number as a list of characters
        stack = []  # Stack to reverse the order of numbers for 'D' pattern
        
        # Iterate over the pattern and use digits 1 to n+1
        for i in range(n + 1):
            # Push the current digit (i + 1) into the stack
            stack.append(str(i + 1))
            
            # If we reach the end of the pattern or encounter an 'I'
            if i == n or pattern[i] == 'I':
                # Pop all elements from the stack to ensure correct order
                while stack:
                    result.append(stack.pop())
        
        # Join the list into a string to form the final result
        return ''.join(result)        