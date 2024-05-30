Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/





class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)
