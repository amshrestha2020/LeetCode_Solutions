Given a string s, return the 
lexicographically smallest
 
subsequence
 of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/




from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char not in seen:
                while stack and char < stack[-1] and counter[stack[-1]] > 0:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)

        return ''.join(stack)
