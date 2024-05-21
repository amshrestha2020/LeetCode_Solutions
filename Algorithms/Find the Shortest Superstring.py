Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.

 

Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
 

Constraints:

1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.






from itertools import permutations

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def get_overlap_len(word1: str, word2: str) -> int:
            for i in range(min(len(word1), len(word2)), 0, -1):
                if word1.endswith(word2[:i]):
                    return i
            return 0

        n = len(words)
        overlap = [[0] * n for _ in range(n)]

        # Precompute overlap between every pair of words
        for i in range(n):
            for j in range(n):
                if i != j:
                    overlap[i][j] = get_overlap_len(words[i], words[j])

        # Initialize dp table
        dp = [[""] * n for _ in range(1 << n)]

        # Populate dp table
        for mask in range(1, 1 << n):
            for bit in range(n):
                if mask & (1 << bit):
                    if mask == 1 << bit:
                        dp[mask][bit] = words[bit]
                    else:
                        for prev_bit in range(n):
                            if prev_bit != bit and mask & (1 << prev_bit):
                                new_overlap = overlap[prev_bit][bit]
                                new_str = dp[mask ^ (1 << bit)][prev_bit] + words[bit][new_overlap:]
                                if dp[mask][bit] == "" or len(new_str) < len(dp[mask][bit]):
                                    dp[mask][bit] = new_str

        # Find the shortest string by trying all possible end points
        min_len = float('inf')
        end_point = -1
        for i in range(n):
            if len(dp[(1 << n) - 1][i]) < min_len:
                min_len = len(dp[(1 << n) - 1][i])
                end_point = i

        return dp[(1 << n) - 1][end_point]
