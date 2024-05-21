Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
 

Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"
 

Constraints:

0 <= a, b <= 100
It is guaranteed such an s exists for the given a and b.



class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a or b:
            if len(res) >= 2 and res[-1] == res[-2]:
                is_b = res[-1] == 'a'
            else:
                is_b = a < b
            if is_b:
                b -= 1
                res.append('b')
            else:
                a -= 1
                res.append('a')
        return "".join(res)
