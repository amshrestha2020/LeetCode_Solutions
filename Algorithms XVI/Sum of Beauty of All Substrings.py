The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.





class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        
        # Iterate over all possible substrings
        for i in range(n):
            freq = [0] * 26  # Frequency array for characters 'a' to 'z'
            for j in range(i, n):
                # Update frequency for the current character
                freq[ord(s[j]) - ord('a')] += 1
                
                # Get the frequencies that are non-zero
                non_zero_freq = [f for f in freq if f > 0]
                
                if non_zero_freq:
                    max_freq = max(non_zero_freq)
                    min_freq = min(non_zero_freq)
                    beauty = max_freq - min_freq
                    total_beauty += beauty
        
        return total_beauty        