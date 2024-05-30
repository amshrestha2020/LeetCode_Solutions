Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = start = 0
        for i, ch in enumerate(s):
            if ch in char_map and start <= char_map[ch]:
                start = char_map[ch] + 1
            else:
                max_length = max(max_length, i - start + 1)
            char_map[ch] = i
        return max_length
