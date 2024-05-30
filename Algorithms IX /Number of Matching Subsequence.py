Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.







from typing import List
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Create a dictionary to store the indices of each character in s
        indices = defaultdict(list)
        for i, char in enumerate(s):
            indices[char].append(i)

        def is_subsequence(word):
            # Initialize the current index to -1
            curr_index = -1
            for char in word:
                # If the character is not in s, return False
                if char not in indices:
                    return False
                # Find the index of the character in s that is greater than the current index
                i = bisect.bisect_right(indices[char], curr_index)
                # If there is no such index, return False
                if i == len(indices[char]):
                    return False
                # Update the current index
                curr_index = indices[char][i]
            return True

        # Count the number of words that are a subsequence of s
        count = sum(is_subsequence(word) for word in words)

        return count

