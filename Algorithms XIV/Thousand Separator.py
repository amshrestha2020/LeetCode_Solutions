Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
 

Constraints:

0 <= n <= 231 - 1





class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        return '.'.join(n[::-1][i:i+3] for i in range(0, len(n), 3))[::-1]
