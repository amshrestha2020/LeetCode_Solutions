Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.



from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_count = Counter()
        
        for i, char in enumerate(s2):
            window_count[char] += 1
            
            # If window size is larger than s1, remove the leftmost character from the window
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1
            
            # If the frequency counts match, return True
            if window_count == s1_count:
                return True
        
        return False

