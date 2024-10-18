You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length



class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        
        # Count the frequency of 'a', 'b', and 'c' in the entire string
        count_a = s.count('a')
        count_b = s.count('b')
        count_c = s.count('c')

        # If there are fewer than k occurrences of 'a', 'b', or 'c', return -1
        if count_a < k or count_b < k or count_c < k:
            return -1
        
        # Now we try to find the maximum middle part that we can leave out
        total_count = {'a': count_a, 'b': count_b, 'c': count_c}
        
        # We need to leave out a segment such that at least `k` of each char is still covered from the two ends.
        # Now, let's use sliding window to find the largest middle segment that leaves the conditions valid
        left = 0
        max_len = 0
        window_count = {'a': 0, 'b': 0, 'c': 0}
        
        # Sliding window over the string
        for right in range(n):
            window_count[s[right]] += 1
            
            # Keep shrinking the window if we've left too many of any character
            while window_count['a'] > total_count['a'] - k or \
                  window_count['b'] > total_count['b'] - k or \
                  window_count['c'] > total_count['c'] - k:
                window_count[s[left]] -= 1
                left += 1
            
            # Track the maximum length of the window (middle part) that can be left out
            max_len = max(max_len, right - left + 1)
        
        # The result is total length minus the largest window length that can be left out
        return n - max_len        