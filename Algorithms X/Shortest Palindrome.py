You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.




class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == n:
            return s
        remain = s[i:]
        return remain[::-1] + self.shortestPalindrome(s[:i]) + s[i:]

