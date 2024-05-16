Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.





class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Concatenate two copies of the string and remove the first and last characters
        temp = (s + s)[1:-1]
        
        # If the original string is a repeated substring pattern, it must be a substring of temp
        return s in temp
