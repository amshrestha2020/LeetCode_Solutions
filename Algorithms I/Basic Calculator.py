Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.



class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0  # For the on-going result
        sign = 1  # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':
                # Evaluate the expression to the left
                # with result, sign, operand
                res += sign * operand
                # Save the recently encountered '+' sign
                sign = 1
                # Reset operand
                operand = 0

            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                # Push the result and sign on to the stack
                # for later use, as result/sign will be updated
                # for the evaluation of sub-expression
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif ch == ')':
                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand
                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop()  # stack pop 1, where '+' = 1, '-' = -1 
                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                res += stack.pop()  # stack pop 2
                # Reset the operand
                operand = 0

        return res + sign * operand

