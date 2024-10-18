You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

 

Example 1:

Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
Example 2:

Input: word1 = "abcc", word2 = "aab"
Output: true
Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
Example 3:

Input: word1 = "abcde", word2 = "fghij"
Output: true
Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 consist of only lowercase English letters.




class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        from collections import defaultdict

        # Maps to store the frequency of each character
        w1 = defaultdict(int)
        w2 = defaultdict(int)
        
        # Helper functions to add and remove characters
        def add(map, c):
            map[c] += 1

        def remove(map, c):
            if map[c] == 1:
                del map[c]
            else:
                map[c] -= 1

        # Fill the frequency maps
        for c in word1:
            add(w1, c)
        for c in word2:
            add(w2, c)

        # Get the keys (distinct characters) of both maps
        k1 = list(w1.keys())
        k2 = list(w2.keys())

        # Check all possible swaps
        for c1 in k1:
            for c2 in k2:
                remove(w1, c1)
                remove(w2, c2)
                add(w1, c2)
                add(w2, c1)
                
                if len(w1) == len(w2):
                    return True

                # Revert the changes
                remove(w1, c2)
                remove(w2, c1)
                add(w1, c1)
                add(w2, c2)

        return False
        