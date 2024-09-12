You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.


class Solution:
    def stack_to_string(self, st):
        str_chars = []
        while st:
            str_chars.append(st.pop())
        return ''.join(reversed(str_chars))
    
    def do_ab(self, s, x, y, ans, st):
        # Process the string to remove "ab" and accumulate points
        for c in s:
            if c == 'b' and st and st[-1] == 'a':
                st.pop()
                ans += x
            else:
                st.append(c)
        return ans
    
    def do_ba(self, s, x, y, ans, st):
        # Process the string to remove "ba" and accumulate points
        for c in s:
            if c == 'a' and st and st[-1] == 'b':
                st.pop()
                ans += y
            else:
                st.append(c)
        return ans
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        st = []
        
        if x > y:
            res = self.do_ab(s, x, y, 0, st)
            s = self.stack_to_string(st)
            res += self.do_ba(s, x, y, 0, st)
        else:
            res = self.do_ba(s, x, y, 0, st)
            s = self.stack_to_string(st)
            res += self.do_ab(s, x, y, 0, st)
        
        return res