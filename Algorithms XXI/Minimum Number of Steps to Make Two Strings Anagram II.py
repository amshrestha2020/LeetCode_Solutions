You are given two strings s and t. In one step, you can append any character to either s or t.

Return the minimum number of steps to make s and t anagrams of each other.

An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "leetcode", t = "coats"
Output: 7
Explanation: 
- In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
- In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
"leetcodeas" and "coatsleede" are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
Example 2:

Input: s = "night", t = "thing"
Output: 0
Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.
 

Constraints:

1 <= s.length, t.length <= 2 * 105
s and t consist of lowercase English letters.




class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        freq_s = Counter(s)
        freq_t = Counter(t)
        
        # Calculate the total number of adjustments needed
        steps = 0
        
        # For characters in s that are in excess compared to t
        for char in freq_s:
            if freq_s[char] > freq_t[char]:
                steps += freq_s[char] - freq_t[char]
        
        # For characters in t that are in excess compared to s
        for char in freq_t:
            if freq_t[char] > freq_s[char]:
                steps += freq_t[char] - freq_s[char]
        
        return steps