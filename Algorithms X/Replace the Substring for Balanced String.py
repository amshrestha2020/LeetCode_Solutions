You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
 

Constraints:

n == s.length
4 <= n <= 105
n is a multiple of 4.
s contains only 'Q', 'W', 'E', and 'R'.





class Solution:
    def balancedString(self, s: str) -> int:
        # Initialize a frequency map for the characters Q, W, E, R
        freq = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}

        # Populate the frequency map with the counts of each character in the input string
        for c in s:
            freq[c] += 1

        # Calculate the target frequency for each character to balance the string
        target = len(s) // 4
        minLen = len(s)
        left = 0

        # Use a sliding window to find the minimum length of the substring to be replaced
        for right in range(len(s)):
            freq[s[right]] -= 1

            # Check if the current window is balanced
            while left < len(s) and all(freq[c] <= target for c in 'QWER'):
                minLen = min(minLen, right - left + 1)
                freq[s[left]] += 1
                left += 1

        return minLen
