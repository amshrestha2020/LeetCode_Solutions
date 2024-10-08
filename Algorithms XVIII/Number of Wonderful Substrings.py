A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.




class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Dictionary to store how many times a prefix xor appears
        prefix_count = {0: 1}  # Base case: prefix 0 is seen once
        current_xor = 0
        result = 0
        
        # Iterate over each character in the word
        for char in word:
            # Update the current xor bitmask for this character
            # 'a' corresponds to bit 0, 'b' to bit 1, ..., 'j' to bit 9
            current_xor ^= (1 << (ord(char) - ord('a')))
            
            # If this exact xor has been seen before, it means the substring between
            # the previous occurrence and here has all even counts (wonderful substring)
            result += prefix_count.get(current_xor, 0)
            
            # We also check for all possible cases where exactly one bit is flipped
            # which would mean one character has an odd count and all others have even counts
            for i in range(10):
                result += prefix_count.get(current_xor ^ (1 << i), 0)
            
            # Update the count of this prefix xor in the dictionary
            prefix_count[current_xor] = prefix_count.get(current_xor, 0) + 1
        
        return result