Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

 

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 

Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.



class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word, s):
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)
        
        dictionary.sort(key=lambda x: (-len(x), x))  # Sort by length and lexicographical order
        
        for word in dictionary:
            if is_subsequence(word, s):
                return word
        
        return ""
