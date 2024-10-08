An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

Example 1:

Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
Example 2:

Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_length = 1  # To store the maximum length found
        current_length = 1  # To store the current continuous substring length

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            # Check if the current character is consecutive to the previous one
            if ord(s[i]) == ord(s[i - 1]) + 1:
                current_length += 1  # Increment current length
            else:
                current_length = 1  # Reset current length
            
            max_length = max(max_length, current_length)  # Update max_length if needed

        return max_length        