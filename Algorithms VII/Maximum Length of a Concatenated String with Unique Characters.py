You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.




from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Filter out the strings that have duplicate characters
        arr = [a for a in arr if len(set(a)) == len(a)]
        
        # Depth-first search
        def dfs(idx, path):
            if idx == len(arr):
                return len(path)
            else:
                taken = 0
                if not set(arr[idx]) & set(path):
                    taken = dfs(idx + 1, path + arr[idx])
                not_taken = dfs(idx + 1, path)
                return max(taken, not_taken)
        
        return dfs(0, "")
