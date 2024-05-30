Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

 

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".
 

Constraints:

1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.




class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2: return 0
        pairs = [(s1, s2)]
        visited = set([tuple(pairs)])
        queue = collections.deque([(pairs, 0)])
        while queue:
            pairs, d = queue.popleft()
            s1, s2 = pairs[0]
            if s1 == s2:
                return d
            for new_pairs in self.neighbors(pairs):
                new_pairs_tuple = tuple(new_pairs)
                if new_pairs_tuple not in visited:
                    visited.add(new_pairs_tuple)
                    queue.append((new_pairs, d + 1))

    def neighbors(self, pairs):
        s1, s2 = pairs[0]
        i = 0
        while s1[i] == s2[i]:
            i += 1
        res = []
        for j in range(i + 1, len(s1)):
            if s1[j] == s2[i]:
                new_s1 = s1[:i] + s1[j] + s1[i + 1:j] + s1[i] + s1[j + 1:]
                res.append([(new_s1, s2)] + pairs[1:])
        return res
