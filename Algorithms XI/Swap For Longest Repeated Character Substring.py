You are given a string text. You can swap two of the characters in the text.

Return the length of the longest substring with repeated characters.

 

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.
Example 3:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.
 

Constraints:

1 <= text.length <= 2 * 104
text consist of lowercase English characters only.




class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import defaultdict
        
        # Step 1: Count the frequency of each character
        char_count = defaultdict(int)
        for ch in text:
            char_count[ch] += 1
        
        # Step 2: Create groups of consecutive identical characters
        groups = []
        i = 0
        while i < len(text):
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j
        
        # Step 3: Calculate the maximum length considering the two cases
        max_length = 0
        for i in range(len(groups)):
            ch, length = groups[i]
            # Case 1: Length of this group, extended by one if there are extra characters
            max_length = max(max_length, min(length + 1, char_count[ch]))
            
            # Case 2: Merge with the next group if possible
            if i + 2 < len(groups) and groups[i + 2][0] == ch and groups[i + 1][1] == 1:
                merged_length = groups[i][1] + groups[i + 2][1]
                max_length = max(max_length, min(merged_length + 1, char_count[ch]))
        
        return max_length
