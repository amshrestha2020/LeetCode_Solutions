You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.






from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Find the maximum frequency of each letter in words2
        max_count2 = Counter()
        for word in words2:
            count = Counter(word)
            for letter, freq in count.items():
                max_count2[letter] = max(max_count2[letter], freq)

        # Check if every word in words1 contains at least these many letters
        result = []
        for word in words1:
            count1 = Counter(word)
            if all(count1[letter] >= freq for letter, freq in max_count2.items()):
                result.append(word)

        return result
