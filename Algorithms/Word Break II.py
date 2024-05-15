Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(index):
            # Return the cached solution if it exists.
            if index in memo:
                return memo[index]
            # Base case: if we have reached the end of the string,
            # return an empty list.
            if index == len(s):
                return [[]]
            
            result = []
            # Try all possible word lengths from the current index.
            for endIndex in range(index + 1, len(s) + 1):
                word = s[index:endIndex]
                # If the word is in the wordSet, then recurse on the remainder
                # of the string and add the word to the front of each valid string.
                if word in wordSet:
                    for subsentence in dfs(endIndex):
                        result.append([word] + subsentence)
            # Cache the result.
            memo[index] = result
            return result

        # For each valid sentence, join the words into a string with spaces between them.
        return [" ".join(words) for words in dfs(0)]


