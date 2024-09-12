Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(path, left, right, res):
            if left > right or left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(path)
                return
            dfs(path + '(', left - 1, right, res)
            dfs(path + ')', left, right - 1, res)
        
        res = []
        dfs('', n, n, res)
        return res

