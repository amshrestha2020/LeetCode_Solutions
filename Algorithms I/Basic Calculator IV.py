Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified expression, such as ["-1*a","14"]

An expression alternates chunks and symbols, with a space separating each chunk and symbol.
A chunk is either an expression in parentheses, a variable, or a non-negative integer.
A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like "2x" or "-x".
Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

For example, expression = "1 + 2 * 3" has an answer of ["7"].
The format of the output is as follows:

For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
For example, we would never write a term like "b*a*c", only "a*b*c".
Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
For example, "a*a*b*c" has degree 4.
The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"].
Terms (including constant terms) with coefficient 0 are not included.
For example, an expression of "0" has an output of [].
Note: You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

 

Example 1:

Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
Output: ["-1*a","14"]
Example 2:

Input: expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
Output: ["-1*pressure","5"]
Example 3:

Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
Output: ["1*e*e","-64"]
 

Constraints:

1 <= expression.length <= 250
expression consists of lowercase English letters, digits, '+', '-', '*', '(', ')', ' '.
expression does not contain any leading or trailing spaces.
All the tokens in expression are separated by a single space.
0 <= evalvars.length <= 100
1 <= evalvars[i].length <= 20
evalvars[i] consists of lowercase English letters.
evalints.length == evalvars.length
-100 <= evalints[i] <= 100






from collections import Counter
from typing import List
from functools import cmp_to_key

class Expr:
    def __init__(self):
        self.coef = 0
        self.vars = []

    def getVal(self):
        if not self.coef:
            return ""
        if not self.vars:
            return str(self.coef)
        return str(self.coef) + "*" + "*".join(self.vars)

def mul(expr1, expr2):
    ret = Expr()
    ret.coef = expr1.coef * expr2.coef
    if ret.coef == 0:
        return ret
    ret.vars = list(sorted(expr1.vars + expr2.vars))
    return ret

def mergeExpr(stack, signs, expr):
    sign = signs[-1][-1]
    if sign == "+":
        stack[-1].append([expr])
    elif sign == "-":
        expr.coef = - expr.coef
        stack[-1].append([expr])
    elif sign == "*":
        last = stack[-1][-1]
        temp = []
        for prev in last:
            temp.append(mul(prev, expr))
        stack[-1][-1] = temp
    signs[-1].pop()

def mergeGroup(stack, signs, group):
    sign = signs[-1][-1]
    if sign == "+":
        stack[-1].append(group)    
    elif sign == "-":
        temp = []
        for expr in group:
            expr.coef = -expr.coef
            temp.append(expr)   
        stack[-1].append(temp)
    elif sign == "*":
        last = stack[-1].pop()
        temp = []
        for expr1 in last:
            for expr2 in group:
                temp.append(mul(expr1, expr2))
        stack[-1].append(temp)
    signs[-1].pop()

def compare(c, d):
    a, b = c.split("*"), d.split("*")
    if len(a) != len(b):
        return len(b) - len(a)
    return 1 if a > b else -1

def getSum(curLevel):
    exprs = {"":0}
    for groups in curLevel:
        for expr in groups:
            if not expr.vars:
                exprs[""] += expr.coef
            else:
                key = "*".join(expr.vars)
                if key not in exprs:
                    exprs[key] = expr
                else:
                    exprs[key].coef += expr.coef
    ret = [exprs[key] for key in sorted(exprs.keys(), key=cmp_to_key(compare)) if key != "" and exprs[key].coef]

    if exprs[""] != 0:
        temp = Expr()
        temp.coef = exprs[""]
        ret.append(temp)
    return ret

def calculate(s, a, b):
    stack, signs = [[]], [["+"]]
    i, n = 0, len(s)
    dic = {x:y for x, y in zip(a, b)}
    while i < n:
        if s[i] == " ":
            i += 1
            continue
        if s[i].isalpha():
            expr = Expr()
            temp = s[i]
            while i+1 < n and s[i+1].isalpha():
                temp += s[i+1]
                i += 1
            if temp in dic:
                expr.coef = dic[temp]
            else:
                expr.coef = 1
                expr.vars = [temp]
            mergeExpr(stack, signs, expr)
        elif s[i].isdigit():
            expr = Expr()
            num = int(s[i])
            while i+1 < n and s[i+1].isdigit():
                num = num * 10 + int(s[i+1])
                i += 1
            expr.coef = num
            mergeExpr(stack, signs, expr)
        elif s[i] in "+-*":
            signs[-1].append(s[i])
        elif s[i] == "(":
            stack.append([])
            signs.append(["+"])
        elif s[i] == ")":
            curLevel = getSum(stack.pop())
            signs.pop()
            mergeGroup(stack, signs, curLevel)
        i += 1
    res = getSum(stack.pop())
    return [expr.getVal() for expr in res]

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        return calculate(expression, evalvars, evalints)
