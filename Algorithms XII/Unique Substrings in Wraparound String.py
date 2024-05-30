We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so base will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string s, return the number of unique non-empty substrings of s are present in base.

 

Example 1:

Input: s = "a"
Output: 1
Explanation: Only the substring "a" of s is in base.
Example 2:

Input: s = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of s in base.
Example 3:

Input: s = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of s in base.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.




class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Initialize a list to store the maximum length of unique substring end with each letter
        dp = [0] * 26
        length = 0

        for i in range(len(s)):
            # If the current character and the previous character are adjacent in the alphabet (circularly), increase the length
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
                length += 1
            else:
                length = 1

            # Update the maximum length of unique substring end with the current character
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)

        # The sum of dp is the total number of unique substrings
        return sum(dp)
