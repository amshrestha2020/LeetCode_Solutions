You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.





class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter
        from typing import List


        count = Counter(words)
        length = 0
        has_center = False
        
        for word, cnt in count.items():
            reverse_word = word[::-1]
            
            if word == reverse_word:  # If the word is a palindrome itself (e.g., "gg")
                # Each pair contributes 4 to the length
                length += (cnt // 2) * 4
                # If there's an odd count, we can place one in the center
                if cnt % 2 == 1:
                    has_center = True
            elif reverse_word in count:  # If the word can pair with its reverse
                if count[reverse_word] > 0:  # Only count if the reverse is available
                    pairs = min(cnt, count[reverse_word])
                    length += pairs * 4  # Each pair contributes 4 to the length
                    # After counting pairs, set their counts to 0 to avoid double counting
                    count[reverse_word] = 0
                    
        # If we have any string that can serve as a center
        if has_center:
            length += 2
            
        return length