Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.




class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i + 1
                else:
                    stack.pop()
                    if not stack:
                        max_length = max(max_length, i - start + 1)
                    else:
                        max_length = max(max_length, i - stack[-1])
        
        return max_length
